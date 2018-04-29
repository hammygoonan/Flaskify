from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app(config="config.development"):
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)
    db.app = app
    db.init_app(app)

    blueprints(app)

    return app


def blueprints(app):
    from flaskify.views.base import base_blueprint
    from flaskify.views.song import songs_blueprint
    from flaskify.views.album import album_blueprint
    from flaskify.views.artist import artist_blueprint
    app.register_blueprint(base_blueprint)
    app.register_blueprint(songs_blueprint, url_prefix='/songs')
    app.register_blueprint(album_blueprint, url_prefix='/albums')
    app.register_blueprint(artist_blueprint, url_prefix='/artists')
