import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = "dev",
        DATABASE = os.path.join(app.instance_path, "flaskr.sqlite"),

        UPLOAD_FOLDER = os.path.join(
            app.instance_path, "uploads"),
        IMAGE_UPLOAD_FOLDER = os.path.join(
            app.instance_path, "uploads/images"),
        IMAGE_ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import (
        db, auth, upload, about, solve, home
    )

    db.init_app(app)
    app.register_blueprint(auth.bp)

    app.register_blueprint(upload.bp)

    # from . import blog
    # app.register_blueprint(blog.bp)

    app.register_blueprint(about.bp)
    app.register_blueprint(solve.bp)
    app.register_blueprint(home.bp)

    # app.add_url_rule("/", endpoint="index")

    return app
