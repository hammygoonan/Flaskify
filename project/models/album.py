"""Album Model."""

import datetime
from sqlalchemy import event

from project import db


album_artists = db.Table(
    'album_artists',
    db.Column('album_id', db.Integer, db.ForeignKey('albums.id')),
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'))
)


class Album(db.Model):
    """Album Model."""

    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    year = db.Column(db.Integer())
    last_updated = db.Column(db.DateTime)

    album_artists = db.relationship('Artist', secondary='album_artists',
                                    backref='artist_albums')

    def __init__(self, **kwargs):
        """Initialise."""
        self.title = kwargs.get('title')
        self.album_artists = kwargs.get('album_artists', [])
        self.year = kwargs.get('year')
        self.last_updated = datetime.datetime.utcnow()

    @property
    def songs(self):
        songs = []
        for album_song in self.album_songs:
            song = album_song.song
            song.track_no = album_song.track_no
            songs.append(song)
        return songs

    def serialise(self):
        """Serialise data for JSON.

        :return: Dict
        """
        serial = {
            'id': self.id,
            'title': self.title,
            'album_artists': [artist.name for artist in self.album_artists]
        }
        return serial


@event.listens_for(Album, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()
