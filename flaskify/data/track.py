"""Classes for absract track class.

:copyright: (c) 2018 Hammy Goonan
"""


from os import path
from flask import current_app


class Track():
    """Abstract class for media types."""

    def __init__(self, path):
        """Initalise track.

        :param path: file path
        """
        self.path = path

    @classmethod
    def get_details(cls, path):
        """Class method to instantiate relevant media class."""
        f_type = path.split('.')[-1]
        for sub_class in cls.__subclasses__():
            if f_type == sub_class.__name__.lower():
                return sub_class(path)
        raise Exception('This file type is not supported.')

    def get_file_path(self):
        """Return full file path."""
        if path.isfile(path.join(current_app.config['MUSIC_DIR'], self.path)):
            return path.join(current_app.config['MUSIC_DIR'], self.path)
        if path.isfile(self.path):
            return self.path

    def get_title(self):
        """Return title. To be extended."""
        pass

    def get_artists(self):
        """Return artists. To be extended."""
        pass

    def get_album_artists(self):
        """Return album artists. To be extended."""
        pass

    def get_album_year(self):
        """Return title. To be extended."""
        pass

    def get_album_pic(self):
        """Return album year. To be extended."""
        pass

    def get_track_album(self):
        """Return track album. To be extended."""
        pass

    def get_track_genre(self):
        """Return track genre. To be extended."""
        pass

    def get_track_copyright(self):
        """Return track copyright. To be extended."""
        pass

    def get_track_publisher(self):
        """Return track publisher. To be extended."""
        pass

    def get_track_number(self):
        """Return track number. To be extended."""
        pass
