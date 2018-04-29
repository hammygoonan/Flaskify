import datetime
from flask import url_for
from flask import current_app
from sqlalchemy import event
from flaskify import db


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
    path = db.Column(db.String(255), nullable=False, unique=True)
    last_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    artists = db.relationship('Artist', secondary=song_artists, backref='songs')
    albums = db.relationship('Album', secondary='album_songs')

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.path = kwargs.get('path')
        self.last_updated = kwargs.get('last_updated')

    def serialise(self):
        return {
            'id': self.id,
            'title': self.title,
            'last_updated': self.last_updated,
            'url': url_for('songs.song', id=self.id),
            'src': url_for(
                'songs.song_file',
                filename=self.path.replace(current_app.config['MUSIC_DIR'], '')[1:]
            ),
            'artists': [
                {
                    'id': artist.id,
                    'name': artist.name,
                    'url': url_for('artists.artist', id=self.id)
                }
                for artist in self.artists
            ],
            'albums': [
                {
                    'id': album.id,
                    'title': album.title,
                    'url': url_for('albums.album', id=self.id)
                }
                for album in self.albums
            ]
        }


@event.listens_for(Song, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()


class AlbumSong(db.Model):
    __tablename__ = 'album_songs'

    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), primary_key=True)
    track_no = db.Column('track_no', db.Integer)

    song = db.relationship('Song', backref='song_albums')
    album = db.relationship('Album', backref='album_songs')
