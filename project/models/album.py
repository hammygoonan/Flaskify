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
    name = db.Column(db.String(255))
    year = db.Column(db.Integer())
    last_updated = db.Column(db.DateTime)

    album_artists = db.relationship('Artist', secondary='album_artists',
                                    backref='albums')

    # songs = db.relationship('AlbumSong', backref='album')

    # genre = db.relationship('Genre', secondary=genre, backref='albums')

    def __init__(self, name, **kwargs):
        """Initialise."""
        self.name = name
        self.album_artists = kwargs.get('album_artists', [])
        self.year = kwargs.get('year')
        # self.genre = kwargs.get('genre')
        self.last_updated = datetime.datetime.utcnow()

    def serialise(self):
        """Serialise data for JSON.

        :return: Dict
        """
        serial = {
            'name': self.name,
            'album_artists': [artist.name for artist in self.album_artists]
        }
        # for song in self.songs:
        #     serial['songs'].append(song.serialise())
        return serial


@event.listens_for(Album, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()
