"""Basic app file."""

from flask import Flask

from .pages import pages


def create_app(config=None):
    """Aplication factory."""
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(pages)

    return app
