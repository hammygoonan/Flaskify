from mutagen.flac import FLAC
from flaskify.data.track import Track


class Flac(Track):
    """Extract metadata.

    http://help.mp3tag.de/main_tags.html
    """

    def __init__(self, path):
        super().__init__(path)
        self.data = self.get_flac(self.path)

    def get_flac(self, path):
        """Return MP3 object.

        :param path: String, filename relative to MUSIC_DIR.
        :return: :class:`MP3 <MP3>`
        """
        return FLAC(self.get_file_path())

    def get_title(self):
        """Return track title.

        :return: string
        """
        if self.data.get('title'):
            return self.data.get('title')[0]
        return ''

    def get_artists(self):
        if self.data.get('artist'):
            return [artist for artist in self.data.get('artist')]
        return []

    def get_album_artists(self):
        if self.data.get('albumartist'):
            return self.data.get('albumartist')
        return []

    def get_album_year(self):
        if self.data.get('date'):
            return int(self.data.get('date')[0])
        return None

    def get_album_pic(self):
        pass

    def get_track_album(self):
        pass

    def get_track_genre(self):
        if self.data.get('genre'):
            return [genre for genre in self.data.get('genre')]
        return []

    def get_track_copyright(self):
        # TCOP
        pass

    def get_track_publisher(self):
        pass

    def get_track_number(self):
        if self.data.get('tracknumber'):
            return int(self.data.get('tracknumber')[0])
        return None
