import datetime
from sqlalchemy import event
from flask import url_for
from flaskify import db


class Artist(db.Model):
    """Artist Model."""

    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.last_updated = kwargs.get('last_updated')

    def serialise(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_updated': self.last_updated,
            'url': url_for('artists.artist', id=self.id),
            'albums': [
                {
                    'id': album.id,
                    'title': album.title,
                    'url': url_for('albums.album', id=self.id)
                }
                for album in self.albums
            ]
        }


@event.listens_for(Artist, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()
