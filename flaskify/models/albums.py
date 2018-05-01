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
    """Song Album."""

    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    artists = db.relationship('Artist', secondary='album_artists', backref='albums')
    songs = db.relationship('Song', secondary='album_songs')

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.last_updated = kwargs.get('last_updated')

    def serialise(self):
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
                for album_song in self.album_songs
            ]
        }


@event.listens_for(Album, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()
