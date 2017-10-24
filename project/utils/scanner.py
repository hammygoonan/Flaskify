"""Loop over designated directory and look for appropriate files.

It will create new database entries for new files and make educated guesses about artists and song
names.
"""
import os
from flask import current_app
from project import db
from project.data.track import Track
from project.models.artist import Artist
from project.models.album import Album
from project.models.album_song import AlbumSong
from project.models.song import Song


def scan_dir(directory=None):
    """Scan a direcotry and it's sub directories for music files."""
    if directory is None:
        app = current_app
        directory = app.config['MUSIC_DIR']

    for path, directories, files in os.walk(directory):
        if ignore_directory(path, directories, files):
            for f in files:
                track = get_track_details(os.path.join(path, f))
                if track:
                    process_track_data(track)


def ignore_directory(path, directories, files):
    """Check if directory should be scanned. Return boolean."""
    if directories:
        return False
    if 'iTunes' in path:
        return False

    for song in files:
        if song[-4:] in ['.mp3', '.mp4', '.m4a', 'flac', '.ogg']:
            return True

    return False


def get_track_details(path):
    """Return an array of `Track` from an array of file paths.

    :paths list: list of paths to songs.
    :return: array of `class Track`
    """
    track = None
    print(Track.get_details(path))
    try:
        track = Track.get_details(path)
    except:
        print('Error opening {}'.format(path))
    return track


def process_track_data(track):
    """Check to see if track exists in database, then create new Track if required.

    :param track: `class Track`
    :return: None
    """
    track_name = track.get_title()
    print(track_name)
    # track_name = track.get_title()
    # song = create_song(track_name, track.get_file_path())
    # album_name = track.get_track_album()
    # album = create_album(album_name)
    #
    # album_song = AlbumSong()
    # album_song.song = song
    # album_song.album = album
    # album_song.track_no = track.get_track_number()
    # db.session.add(album_song)
    #
    # for artist_name in track.get_artists():
    #     artist = create_artist(artist_name)
    #     song.artists.append(artist)
    #
    # for artist_name in track.get_album_artists():
    #     artist = create_artist(artist_name)
    #     album.album_artists.append(artist)
    #
    # db.session.commit()


def create_artist(name):
    """Either create artist or return existing artist.

    :param name: string
    :return: `class Artist`
    """
    artist = Artist.query.filter_by(name=name).first()
    if artist is None:
        artist = Artist(name=name)
        db.session.add(artist)
        db.session.commit()
    return artist


def create_album(title):
    """Either create album or return existing album.

    :param name: string
    :return: `class Album`
    """
    album = Album.query.filter_by(title=title).first()
    if album is None:
        album = Album(title=title)
        db.session.add(album)
        db.session.commit()
    return album


def create_song(title, path):
    """Either create song or return existing song.

    :param name: string
    :return: `class Song`
    """
    song = Song.query.filter_by(path=path).first()
    if song is None:
        song = Song(title=title, path=path)
        db.session.add(song)
        db.session.commit()
    return song
