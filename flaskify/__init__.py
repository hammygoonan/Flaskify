from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config="config.development"):
    app = Flask(__name__)
    app.config.from_object(config)

    db.app = app
    db.init_app(app)

    return app
