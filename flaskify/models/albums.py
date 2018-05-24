"""Album models.

:copyright: (c) 2018 Hammy Goonan
"""

import datetime
from flask import url_for
from flask import current_app
from sqlalchemy import event
from flaskify import db


album_artists = db.Table(
    'album_artists',
    db.Column('album_id', db.Integer, db.ForeignKey('albums.id')),
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'))
)


class Album(db.Model):
    """Representation of an Album."""

    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    album_art = db.Column(db.Binary())
    last_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    artists = db.relationship('Artist', secondary='album_artists', backref='albums')
    songs = db.relationship('Song', secondary='album_songs')

    def __init__(self, **kwargs):
        """Initialise :class:`Album`.

        :param title: Album title
        :param album_art: Byte representation of album art
        :param last_updated: Date album was last updated
        """
        self.title = kwargs.get('title')
        self.album_art = kwargs.get('album_art')
        self.last_updated = kwargs.get('last_updated')

    def serialise(self):
        """Serialise representation of class.

        :return: dictionary of album.
        :rtype: dict
        """
        return {
            'id': self.id,
            'title': self.title,
            'last_updated': self.last_updated,
            'url': url_for('albums.album', id=self.id),
            'artists': [
                {
                    'id': artist.id,
                    'name': artist.name,
                    'url': url_for('artists.artist', id=self.id)
                }
                for artist in self.artists
            ],
            'songs': [
                {
                    'id': album_song.song.id,
                    'title': album_song.song.title,
                    'last_updated': album_song.song.last_updated,
                    'url': url_for('songs.song', id=album_song.song.id),
                    'track_no': album_song.track_no,
                    'src': url_for(
                        'songs.song_file',
                        filename=album_song.song.path.replace(
                            current_app.config['MUSIC_DIR'], '')[1:]
                    ),
                    'artists': [
                        {
                            'id': artist.id,
                            'name': artist.name,
                            'url': url_for('artists.artist', id=self.id)
                        }
                        for artist in album_song.song.artists
                    ],
                }
                for album_song in sorted(
                    self.album_songs, key=lambda k: track_number_int(k.track_no)
                )
            ]
        }


def track_number_int(track_no):
    if track_no is None:
        return 0
    if type(track_no) == int:
        return track_no
    if '/' in track_no:
        return int(track_no.split('/')[0])
    if '-' in track_no:
        return int(track_no.split('-')[0])
    try:
        return int(track_no)
    except ValueError:
        return 0


@event.listens_for(Album, 'before_update')
def before_update_listener(mapper, connection, target):
    """Update :class:`Album`'s `last_updated` field via listener."""
    target.last_updated = datetime.datetime.utcnow()
