"""Basic app file."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config=None):
    """Aplication factory."""
    app = Flask(__name__)
    app.config.from_object(config)

    db.app = app
    db.init_app(app)

    blueprints(app)

    return app


def blueprints(app):
    from project.views.song import songs_blueprint
    from project.views.album import album_blueprint
    from project.views.artist import artist_blueprint
    app.register_blueprint(songs_blueprint, url_prefix='/songs')
    app.register_blueprint(album_blueprint, url_prefix='/albums')
    app.register_blueprint(artist_blueprint, url_prefix='/artists')
