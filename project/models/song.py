"""Song Model."""

import datetime
from sqlalchemy import event

from project import db


song_artists = db.Table(
    'song_artists',
    db.Column('song_id', db.Integer, db.ForeignKey('songs.id')),
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'))
    )


class Song(db.Model):
    """Song Model."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    last_updated = db.Column(db.DateTime)

    artists = db.relationship('Artist', secondary=song_artists, backref='songs')
    # albums = db.relationship('AlbumSong', backref='song')

    def __init__(self, **kwargs):
        """Initialise model."""
        self.title = kwargs.get('title')
        self.path = kwargs.get('path')
        self.last_updated = datetime.datetime.utcnow()

    def get_url_for(self):
        """Return url for song.

        :return: String, url.
        """
        pass

    def serialise(self):
        """Return serialised data.

        :return: dict
        """
        return {
            'id': self.id,
            'title': self.title,
            'path': self.path,
            'last_updated': self.last_updated
        }


@event.listens_for(Song, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()
