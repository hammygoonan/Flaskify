"""Artist Model."""

import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event

from flaskify import db


class Artist(SQLAlchemy):
    """Artist Model."""

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name):
        """Initialise Model."""
        self.name = name
        self.last_updated = datetime.datetime.utcnow()

    def serialise(self):
        return self.__dict__


@event.listens_for(Artist, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()
