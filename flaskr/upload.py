import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask import current_app
from flask import send_from_directory

from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("upload", __name__, url_prefix = "/upload")

@bp.route("/")
@login_required
def index():
    # db = get_db()
    # posts = db.execute(
    #     "SELECT p.id, title, body, created, author_id, username"
    #     " FROM post p JOIN user u ON p.author_id = u.id"
    #     " ORDER BY created DESC"
    # ).fetchall()

    return render_template("upload/index.html")

@bp.route('/images', methods=('GET', 'POST'))
@login_required
def images():
    if request.method == 'POST':
        if "file" not in request.files:
            flash("No file!")
            return redirect(request.url)

        files = request.files["file"]
        print(files)

        # if file.filename == "":
        #     flash("No selected file!")
        #     return redirect(request.url)
        #
        # if not image_allowed_file(file.filename):
        #     flash("Image extension must be: {}".format(
        #         current_app.config["IMAGE_ALLOWED_EXTENSIONS"]))
        #     return redirect(request.url)
        # if file:
        #     filename = secure_filename(file.filename)
        #     file_extension = filename.rsplit('.', 1)[1].lower()
        #     data = file.read()
        #
        #     db = get_db()
        #     db.execute(
        #         'INSERT INTO raw_image (filename, extension, data)'
        #         ' VALUES (?, ?, ?)',
        #         (filename, file_extension, data)
        #     )
        #     db.commit()

            # filename = secure_filename(file.filename)
            # file.save(
            #     os.path.join(current_app.config["IMAGE_UPLOAD_FOLDER"],
            #     filename
            # ))
            # flash("Ok")
            # return redirect(request.url)



    return render_template('upload/images.html')

@bp.route('/videos', methods=('GET', 'POST'))
@login_required
def videos():
    if request.method == 'POST':
        # title = request.form['title']
        # body = request.form['body']
        # error = None
        #
        # if not title:
        #     error = 'Title is required.'
        #
        # if error is not None:
        #     flash(error)
        # else:
        #     db = get_db()
        #     db.execute(
        #         'INSERT INTO post (title, body, author_id)'
        #         ' VALUES (?, ?, ?)',
        #         (title, body, g.user['id'])
        #     )
        #     db.commit()
        if(True):
            return redirect(url_for('upload.index'))

    return render_template('upload/videos.html')

@bp.route('/download/image/<name>')
def download_image(name):
    return send_from_directory(
        os.path.join(current_app.config["UPLOAD_FOLDER"], "images"),
        name
    )


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

def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def image_allowed_file(filename):
    return allowed_file(
        filename,
        current_app.config["IMAGE_ALLOWED_EXTENSIONS"]
    )
