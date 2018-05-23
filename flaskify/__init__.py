"""Main application entry point.

:copyright: (c) 2018 Hammy Goonan
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from elasticsearch import Elasticsearch

db = SQLAlchemy()


def create_app(config="config.development"):
    """Create application.

    :param config: string representing config object.
    :return: Flask app
    :rtype: :class:`Flask`
    """
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)
    db.app = app
    db.init_app(app)

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    blueprints(app)

    return app


def blueprints(app):
    """Register blueprint for site."""
    from flaskify.views.base import base_blueprint
    from flaskify.views.song import songs_blueprint
    from flaskify.views.album import album_blueprint
    from flaskify.views.artist import artist_blueprint
    app.register_blueprint(base_blueprint)
    app.register_blueprint(songs_blueprint, url_prefix='/songs')
    app.register_blueprint(album_blueprint, url_prefix='/albums')
    app.register_blueprint(artist_blueprint, url_prefix='/artists')
