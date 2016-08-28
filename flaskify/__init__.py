"""Basic app file."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .pages import pages

db = SQLAlchemy()


def create_app(config=None):
    """Aplication factory."""
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(pages)

    db.app = app
    db.init_app(app)

    return app
