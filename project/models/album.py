"""Album Model."""

import datetime
from sqlalchemy import event

from project import db


class Album(db.Model):
    """Album Model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    last_updated = db.Column(db.DateTime)
    # album_artist

    def __init__(self, name, album_artist):
        """Initialise."""
        self.name = name
        self.album_artist = album_artist
        self.last_updated = datetime.datetime.utcnow()

    def serialise(self):
        """Serialise data for JSON.

        :return: Dict
        """
        serial = {
            'name': self.name,
            'artist': [artist.name for artist in self.artist],
            'songs': []
        }
        for song in self.songs:
            serial['songs'].append(song.serialise())
        return serial


@event.listens_for(Album, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()
