import datetime
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


@event.listens_for(Album, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()
