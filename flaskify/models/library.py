"""Application file."""


import os

from flask import current_app
from .artist import Artist
from .album import Album
from .song import Song


class Library():
    """A master class that scans hard drive and creates library object."""

    def __init__(self):
        """Initialise."""
        self.media_dir = current_app.config['MEDIA_DIR']
        self.artists = []
        self.albums = []
        self.songs = []
        self.get_library()

    def get_library(self):
        """Walk file system checking for audio files."""
        for path, directories, files in os.walk(self.media_dir):
            path_bits = path.split('/')
            if self.ignore_directory(path, directories, files):
                artist = self.get_artist(path_bits[-2])
                album = self.get_album(path_bits[-1], artist)
                songs = self.get_songs(files, path, artist, album)
                album.songs = songs

    def get_artist(self, artist_name):
        """Check it see if artist exists, append to list then return artist."""
        artist = list(filter(lambda x: x.name == artist_name, self.artists))
        if not artist:
            artist = Artist(artist_name)
            self.artists.append(artist)
            return artist
        else:
            return artist[0]

    def get_album(self, album_name, artist):
        """Check it see if album exists, append to list then return album."""
        album = list(filter(lambda x: x.name == album_name, self.albums))
        if not album:
            album = Album(album_name, artist)
            self.albums.append(album)
            return album
        else:
            return album[0]

    def get_songs(self, files, path, artist, album):
        """Loop over files and create array of `Song` objects."""
        songs = []
        for song in files:
            songs.append(
                Song(song, os.path.join(path, song), album=album,
                     artist=artist)
            )
        self.songs += songs
        return songs

    def ignore_directory(self, path, directories, files):
        """Check if directory shold be scanned. Return boolean."""
        if directories:
            return False
        if 'iTunes' in path:
            return False

        songs = [song for song in files if song[-4:] in
                 ['.mp3', '.m4a', 'flac', '.ogg']]
        if not songs:
            return False
        return True
