"""Song Model."""

from mutagen.mp3 import MP3


class Song():
    """Song Model."""

    def __init__(self, name, path, **kwargs):
        """Initialise model."""
        self.id = id(self)
        self.name = name
        self.path = path
        self.artist = kwargs.get('artist')
        self.album = kwargs.get('album')
        self.track_no = kwargs.get('track_no')
        self.length = kwargs.get('length')
        self.size = kwargs.get('size')
        self.year = kwargs.get('year')
        if path[-3:] == 'mp3':
            self.get_metadata()

    def get_metadata(self):
        """Get file meta data."""
        audio = MP3(self.path)


    def serialise(self):
        serial = self.__dict__
        serial['album'] = self.album.name
        serial['artist'] = self.artist.name
        return serial
