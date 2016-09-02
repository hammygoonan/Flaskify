from project import db


class AlbumSong(db.Model):
    """Album to Song association."""

    __tablename__ = 'album_songs'

    id = db.Column(db.Integer, primary_key=True)
    song = db.relationship('Song', backref='songs')
    album = db.relationship('Album', backref='albums')
    track_no = db.Column('track_no', db.Integer)
