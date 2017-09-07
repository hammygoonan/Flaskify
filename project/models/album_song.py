from project import db


class AlbumSong(db.Model):
    """Album to Song association."""

    __tablename__ = 'album_songs'

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))

    song = db.relationship('Song', backref='album')
    album = db.relationship('Album', backref='song')
    track_no = db.Column('track_no', db.Integer)
