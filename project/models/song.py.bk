"""Song Model."""

import datetime
from os import path
from sqlalchemy import event
from flask import current_app, url_for
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen.flac import FLAC
from mutagen.mp4 import MP4

from project import db
from .album import Album
from .artist import Artist

artists = db.Table(
    'song_artists',
    db.Column('song_id', db.Integer, db.ForeignKey('songs.id')),
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'))
    )


class Song(db.Model):
    """Song Model."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255))
    file_type = db.Column(db.String(10))
    title = db.Column(db.String(255))
    album_pic = db.Column(db.Text())
    year = db.Column(db.Integer)
    hash = db.Column(db.Text())
    last_updated = db.Column(db.DateTime)
    artists = db.relationship('Artist', secondary=artists,
                              backref='songs')

    file_types = ['mp3', 'mp4', 'm4a', 'flac']

    # albums = db.relationship('AlbumSong', backref='song')

    def __init__(self, path, **kwargs):
        """Initialise model."""
        self.id = id(self)
        self.path = path
        self.file_type = self.get_file_type()
        # self.url_for = self.get_url_for()
        self.meta = self.get_meta()
        self.title = self.get_track_title(kwargs.get('title'))
        self.track_no = self.get_track_number(kwargs.get('track_no'))
        # self.album_pic = self.get_album_pic()
        # self.length = kwargs.get('length')
        # self.size = kwargs.get('size')
        self.year = self.get_track_year(kwargs.get('year'))
        self.mp3_tags = ['APIC', 'COM', 'COMM', 'MCDI', 'POPM', 'PRIV', 'TALB',
                         'TCOM', 'TCON', 'TCOP', 'TDRC', 'TDRL', 'TENC',
                         'TIT1', 'TIT2', 'TLAN', 'TLEN', 'TPE1', 'TPE2',
                         'TPOS', 'TPUB', 'TRCK', 'TSRC', 'TSSE', 'TXXX',
                         'WXXX']
        self.mp4_tags = ['pgap', 'covr', 'soar', '©nam', 'sonm', '©too',
                         'xid ', 'soal', 'cpil', 'disk', 'aART', '©day',
                         'tmpo', 'apID', 'purd', '©gen', '©cmt', '©wrt',
                         'ownr', '©alb', '©ART', 'trkn']
        self.flac_tags = ['totaltracks', 'tracknumber', 'artist', 'composer',
                          'albumartist', 'discnumber', 'genre', 'date',
                          'album', 'comment', 'totaldiscs', 'title',
                          'performer']
        # self.hash = self.get_hash('hash')
        self.artists = self.get_artists(kwargs.get('artists'))
        self.album = self.get_track_album(kwargs.get('album'))
        # self.album_artist = self.get_album_artist(kwargs.get('album_artist'))
        # self.last_updated = datetime.datetime.utcnow()

    def get_file_type(self):
        """Return file type.

        :return: String, file suffix
        """
        f_type = self.path.split('.')[-1]
        if f_type == 'm4a' or f_type == 'm4b':
            f_type == 'mp4'
        if f_type not in self.file_types:
            raise ValueError('Unsupported file type.')
        return f_type

    def get_url_for(self):
        """Return url for song.

        :return: String, url.
        """
        media_dir = current_app.config['MEDIA_DIR']
        static_folder = current_app.static_folder
        static_path = media_dir.replace(static_folder, '')
        return url_for('static', filename='{}/{}'.format(
            static_path[1:], self.path)
        )

    def get_meta(self):
        """Get file meta data."""
        if self.file_type == 'mp3':
            return self.get_mp3(path.join(current_app.config['MEDIA_DIR'],
                                self.path))
        if self.file_type == 'ogg':
            return self.get_ogg(path.join(current_app.config['MEDIA_DIR'],
                                self.path))
        if self.file_type == 'flac':
            return self.get_flac(path.join(current_app.config['MEDIA_DIR'],
                                 self.path))
        if self.file_type == 'm4a' or self.file_type == 'mp4':
            return self.get_mp4(path.join(current_app.config['MEDIA_DIR'],
                                self.path))

    def get_album_pic(self):
        """Get album Artwork.

        Tag: APIC
        """

        if self.file_type == 'mp3':
            field = self.meta.tags.get('APIC:')
            # print(field)
            # if field:
            #     return field.data

        if self.file_type == 'mp4':
            # MP4Cover()
            field = self.meta.tags.get('covr')
            # if field:
            #     return field.covr

        return None

    def get_track_album(self, album=None):
        """Get album name.

        Tag: TALB
        """
        if album:
            return album

        if album:
            if isinstance(album, Album):
                return [album]
            elif isinstance(album, list):
                pass
            elif isinstance(album, str):
                pass
            else:
                raise ValueError(
                    'Album but be a sting, list or `Album` object')

        album_name = self.get_meta_text(mp3='TALB', mp4='soal', flac='album')

        if album_name is None:
            album_name = self.path.split('/')[-2]

        if isinstance(album_name, list):
            album_name = album_name[0]

        artist = self.get_artists()
        Album.query.filter_by(name=album_name)

        return album

    def get_album_name(self):
        """Return artist name as string.

        :return: String, artist name
        """
        if isinstance(self.album, Album):
            return self.album.name
        return self.album

    def get_track_style(self, track):
        """Get track style.

        Tag: TCON
        """
        return self.get_meta_text(mp3='TCON', mp4='©gen', flac='genre')

    def get_track_copyright(self, track):
        """Get track copyright.

        Tag: TCOP
        """
        return self.get_meta_text(mp3='TCOP')

    def get_track_year(self, year=None):
        """Get track date recorded.

        Tag: TDRC
        """
        if year:
            return year

        year = self.get_meta_text(mp3='TDRC')
        if year:
            # ID3TimeStamp to string to int
            return int(year[0].year)
        return year

    def get_track_release_date(self):
        """Get track date recorded.

        Tag: TDRL
        """
        return self.get_meta_text(mp3='TDRL', mp4='day', flac='date')

    def get_track_encoder(self, track):
        """Get track date recorded.

        Tag: TENC
        """
        return self.get_meta_text(mp3='TENC')

    def get_track_title(self, title=None):
        """Get track Title.

        Tag: TIT2
        """
        if title:
            return title
        title = self.get_meta_text(mp3='TIT2', mp4='sonm', flac='title')
        if title is None:
            return self.path.split('/')[-1]
        return title[0]

    def get_track_publisher(self, track):
        """Get track Title.

        Tag: TPUB
        """
        return self.get_meta_text(mp3='TPUB')

    def get_track_number(self, track_number=None):
        """Get track Title.

        Tag: TRCK
        """
        if track_number:
            return track_number
        track_number = self.get_meta_text(mp3='TRCK', mp4='trkn',
                                          flac='tracknumber')

        if track_number is None:
            track_name = self.path.split('/')[-1]
            # :todo: with regex
            return track_name[:2]

        if isinstance(track_number, list):
            if '/' in track_number[0]:
                track_number = track_number[0].split('/')[0]
            elif isinstance(track_number[0], tuple):
                track_number = track_number[0][0]
            else:
                track_number = track_number[0]

        return int(track_number)

    # def get_comment(self, tag):
    #     """Get track comment.
    #
    #     Tag: COMM:<comment type>
    #     """
    #     return self.get_meta_text(tag)

    def get_artists(self, artists=None):
        """Get song artist."""
        # if no artist set but has metadata
        if self.artists:
            return self.artists

        if artists is None:
            artists = self.get_meta_text(mp3='TPE1', mp4='aART', flac='artist')
        # if no artist set an no metadata get from file path
        if artists is None:
            if self.path.split('/')[-3] == 'Music':
                artist_name = self.path.split('/')[-2]
            else:
                artist_name = self.path.split('/')[-2]
            artists = [Artist.get_or_create(artist_name)]
        else:
            # if artists is a list
            if isinstance(artists, list):
                artist_obj = []
                for artist in artists:
                    if isinstance(artist, Artist):
                        artist_obj.append(artist)
                    else:
                        artist_obj.append(Artist.get_or_create(artist))
                return artist_obj
            # if artists is a string
            if isinstance(artists, str):
                return [Artist.get_or_create(artists)]
            # if artists is an object
            if isinstance(artists, Artist):
                return [artists]
        # return empty list if all else fails
        if artists is None:
            artists = []

        return artists

    def get_artist_name(self):
        """Return artist name as list.

        :return: List, artist name
        """
        artist_name = []
        for artist in self.artists:
            if isinstance(artist, Artist):
                artist_name.append(artist.name)
            else:
                artist_name.append(artist)
        return artist_name

    def get_album_artist(self, artist=None):
        """Get song artist."""
        if artist:
            return artist
        artist = self.get_meta_text(mp3='TPE2', mp4='aART', flac='albumartist')
        if artist is None:
            if self.path.split('/')[-3] == 'Music':
                return [self.path.split('/')[-2]]
            return [self.path.split('/')[-3]]
        return artist

    def get_album_artist_name(self):
        """Return album artist name as list.

        :return: List, artist name
        """
        artist_name = []
        for artist in self.album_artist:
            # print(artist.name)
            if isinstance(artist, Artist):
                artist_name.append(artist.name)
            else:
                artist_name.append(artist)
        return artist_name

    def get_meta_text(self, **kwargs):
        """Get text from Meta field.

        :param tag: A tag from tag_list
        :return: tag text or None
        """
        mp3_tag = kwargs.get('mp3')
        mp4_tag = kwargs.get('mp4')
        flac_tag = kwargs.get('flac')
        if self.file_type == 'mp3' and mp3_tag:
            field = self.meta.tags.get(mp3_tag)
            if field:
                return field.text
        if (self.file_type == 'mp4' or self.file_type == 'm4a') and mp4_tag:
            field = self.meta.tags.get(mp4_tag)
            if field:
                return field
        if self.file_type == 'flac' and flac_tag:
            field = self.meta.tags.get(flac_tag)
            if field:
                return field
        return None

    def get_mp3(self, path):
        """Return MP3 object.

        :param path: String, complete path to file.
        :return: :class:`MP3 <MP3>`
        """
        return MP3(path)

    def get_ogg(self, path):
        """Return OGG object.

        :param path: String, complete path to file.
        :return: :class:`OggVorbis <OggVorbis>`
        """
        return OggVorbis(path)

    def get_flac(self, path):
        """Return Flac object.

        :param path: String, complete path to file.
        :return: :class:`FLAC <FLAC>`
        """
        return FLAC(path)

    def get_mp4(self, path):
        """Return M4a object.

        :param path: String, complete path to file.
        :return: :class:`M4A <M4A>`
        """
        return MP4(path)

    def serialise(self):
        """Return serialised data."""
        serial = self.__dict__
        serial.pop('meta')
        serial.pop('mp3_tags')
        serial.pop('path')
        serial.pop('mp4_tags')
        serial.pop('flac_tags')
        serial['album'] = self.get_album_name()
        serial['artist'] = self.get_artist_name()
        serial['album_artist'] = self.get_album_artist_name()
        return serial


@event.listens_for(Song, 'before_update')
def before_update_listener(mapper, connection, target):
    target.last_updated = datetime.datetime.utcnow()
