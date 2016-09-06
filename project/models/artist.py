"""Artist Model."""

import datetime
from sqlalchemy import event

from project import db


class Artist(db.Model):
    """Artist Model."""

    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    last_updated = db.Column(db.DateTime)

    def __init__(self, name):
        """Initialise Model."""
        self.name = name
        self.last_updated = datetime.datetime.utcnow()

    def serialise(self):
        return {'name': self.name}

    @staticmethod
    def get_or_create(name):
        artist = Artist.query.filter_by(name=name).first()
        if artist is None:
            artist = Artist(name)
        return artist


@event.listens_for(Artist, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()
