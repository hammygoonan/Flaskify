"""Album Model."""


class Album():
    """Album Model."""

    def __init__(self, name, artist):
        """Initialise."""
        self.id = id(self)
        self.name = name
        self.artist = artist
        self.songs = []

    def serialise(self):
        serial = {
            'name': self.name,
            'artist': self.artist.name,
            'songs': []
        }
        for song in self.songs:
            serial['songs'].append(song.serialise())
        return serial
