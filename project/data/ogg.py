from mutagen.oggvorbis import OggVorbis
from project.data.track import Track


class Ogg(Track):
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
        return OggVorbis(self.get_file_path())

    def get_title(self):
        """Return track title.

        :return: string
        """
        if self.data.get('TITLE'):
            return self.data.get('TITLE')[0]
        return ''

    def get_artists(self):
        if self.data.get('ARTIST'):
            return [artist for artist in self.data.get('ARTIST')]
        return []

    def get_album_artists(self):
        if self.data.get('ARTIST'):
            return [artist for artist in self.data.get('ARTIST')]
        return []

    def get_album_year(self):
        if self.data.get('DATE'):
            return int(self.data.get('DATE')[0])
        return None

    def get_album_pic(self):
        pass

    def get_track_album(self):
        if self.data.get('ALBUM'):
            return self.data.get('ALBUM')[0]
        return None

    def get_track_genre(self):
        pass
        if self.data.get('GENRE'):
            return [genre for genre in self.data.get('GENRE')]
        return []

    def get_track_copyright(self):
        # TCOP
        pass

    def get_track_publisher(self):
        pass

    def get_track_number(self):
        if self.data.get('TRACKNUMBER'):
            return int(self.data.get('TRACKNUMBER')[0])
        return None
