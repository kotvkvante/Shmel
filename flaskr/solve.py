import os
import enum
from base64 import b64encode

from flask import (
    Blueprint, flash, g, redirect,
    render_template, request, url_for, session,
    jsonify
)
from flask import current_app
from flask import send_from_directory

from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

from flaskr.auth import login_required
from flaskr.db import get_db

@enum.unique
class Solution(enum.IntEnum):
    pointto = 0
    inventory = 1

bp = Blueprint("solve", __name__, url_prefix = "/solve")

@bp.route("/")
@login_required
def index():
    # db = get_db()
    # posts = db.execute(
    #     "SELECT p.id, title, body, created, author_id, username"
    #     " FROM post p JOIN user u ON p.author_id = u.id"
    #     " ORDER BY created DESC"
    # ).fetchall()

    return render_template("solve/index.html")

@bp.route('/pointto', methods=('GET',))
@login_required
def pointto():
    image_row = get_raw_unproc_image();

    # print(type(g.user))
    session["pointto_image_id"] = image_row["id"]
    main_image_data = b64encode(image_row["data"]).decode("utf-8")

    # option = [(name, filename), ]
    options = get_pointto_options()

    return render_template(
        'solve/pointto.html',
        main_image = main_image_data,
        options = options
    )

@bp.route("/pointto_solution", methods=("POST",))
@login_required
def pointto_solution():
    user_id = g.user["id"]
    image_id = session.get("pointto_image_id")
    option = request.form.get("option")
    options = get_pointto_names()
    if (image_id is None) or (option not in options):
        abort(500)

    option_id = get_pointto_option_id(option)

    res = insert_solution_safe(Solution.pointto, (image_id, option_id, user_id))
    if not res:
        abort(500)

    image_row = get_raw_unproc_image();
    main_image_data = b64encode(image_row["data"]).decode("utf-8")

    # data = {"status": "success", "image_data": main_image_data}
    return render_template(
        "solve/pointto_img.html",
        main_image = main_image_data
    )



@bp.route("/inventory", methods=("GET",))
@login_required
def inventory():

    return render_template(
        "solve/inventory.html",
        # main_image = main_image,
        # options = options
    )

def insert_solution_safe(stype, sdata):
    if stype not in Solution:
        return False
    if sdata is None:
        return False

    res = insert_solution(stype, sdata)
    return res

def insert_solution(stype, sdata):
    db = get_db()
    if stype == Solution.pointto:
        db = get_db()
        db.execute(
            'INSERT INTO pointto_solution (image_id, option_id, user_id)'
            ' VALUES (?, ?, ?)',
            (sdata)
        )
        db.commit()
        return True
    elif stype == Solution.inventory:
        abort(404)
    return False

def get_pointto_names():
    path = os.path.join(current_app.static_folder, 'block_textures')
    files = os.listdir(path)
    names  = [f.rsplit('.', 1)[0] for f in files]
    return names

def get_pointto_options():
    path = os.path.join(current_app.static_folder, 'block_textures')
    files = os.listdir(path)
    names  = [f.rsplit('.', 1)[0] for f in files]
    fname  = [os.path.join("block_textures", file) for file in files]
    return zip(names, fname)

def get_raw_unproc_image():
    raw_image = get_db().execute(
        # "SELECT id, data FROM raw_image WHERE processed = FALSE"
        "SELECT id, data FROM raw_image ORDER BY RANDOM() LIMIT 1"
    ).fetchone()

    if raw_image is None:
        print("No unprocessed images.")

    return raw_image

def get_pointto_option_id(option):
    return 1
# def get_post(id, check_author=True):
#     post = get_db().execute(
#         'SELECT p.id, title, body, created, author_id, username'
#         ' FROM post p JOIN user u ON p.author_id = u.id'
#         ' WHERE p.id = ?',
#         (id,)
#     ).fetchone()
#
#     if post is None:
#         abort(404, f"Post id {id} doesn't exist.")
#
#     if check_author and post['author_id'] != g.user['id']:
#         abort(403)
#
#     return post

# @bp.route("/<int:id>/update", methods=("GET", "POST"))
# @login_required
# def update(id):
#     post = get_post(id)
#
#     if request.method == "POST":
#         title = request.form["title"]
#         body  = request.form["body"]
#         error = None
#
#         if not title:
#             error = "Title is required."
#
#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 "UPDATE post SET title = ?, body = ?"
#                 " WHERE id = ?",
#                 (title, body, id)
#             )
#             db.commit()
#             return redirect(url_for("blog.index"))
#
#     return render_template("blog/update.html", post=post)

# @bp.route('/<int:id>/delete', methods=('POST',))
# @login_required
# def delete(id):
#     get_post(id)
#     db = get_db()
#     db.execute('DELETE FROM post WHERE id = ?', (id,))
#     db.commit()
#     return redirect(url_for('blog.index'))
