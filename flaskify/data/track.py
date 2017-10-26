from os import path
from flask import current_app


class Track():

    def __init__(self, path):
        self.path = path

    @classmethod
    def get_details(cls, path):
        f_type = path.split('.')[-1]
        for sub_class in cls.__subclasses__():
            if f_type == sub_class.__name__.lower():
                return sub_class(path)
        raise Exception('This file type is not supported.')

    def get_file_path(self):
        if path.isfile(path.join(current_app.config['MUSIC_DIR'], self.path)):
            return path.join(current_app.config['MUSIC_DIR'], self.path)
        if path.isfile(self.path):
            return self.path

    def get_title(self):
        pass

    def get_artists(self):
        pass

    def get_album_artists(self):
        pass

    def get_album_year(self):
        pass

    def get_album_pic(self):
        pass

    def get_track_album(self):
        pass

    def get_track_genre(self):
        pass

    def get_track_copyright(self):
        pass

    def get_track_publisher(self):
        pass

    def get_track_number(self):
        pass
