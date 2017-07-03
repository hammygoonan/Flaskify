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

    def get_title(self):
        pass

    def get_artists(self):
        pass

    def get_album_artists(self):
        pass

    def get_album_title(self):
        pass

    def get_album_year(self):
        pass

    def get_url_for(self):
        pass

    def get_album_pic(self):
        pass

    def get_track_album(self):
        pass

    def get_album_name(self):
        pass

    def get_track_style(self):
        pass

    def get_track_copyright(self):
        pass

    def get_track_release_date(self):
        pass

    def get_track_encoder(self):
        pass

    def get_track_publisher(self):
        pass

    def get_track_number(self):
        pass
