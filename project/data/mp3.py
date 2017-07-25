from mutagen.mp3 import MP3
from .track import Track


class Mp3(Track):
    """Extract metadata.

    http://help.mp3tag.de/main_tags.html
    """

    def __init__(self, path):
        super().__init__(path)
        self.data = self.get_mp3(self.path)

    def get_mp3(self, path):
        """Return MP3 object.

        :param path: String, filename relative to MEDIA_DIR.
        :return: :class:`MP3 <MP3>`
        """
        return MP3(self.get_file_path())

    def get_title(self):
        """Return track title.

        :return: string
        """
        return self.data.get('TIT2').text[0]

    def get_artists(self):
        return self.data.get('TPE1')

    def get_album_artists(self):
        return self.data.get('TPE2')

    # def get_album_title(self):
    #     pass

    def get_album_year(self):
        return self.data.get('TDRC')

    # def get_url_for(self):
    #     pass

    def get_album_pic(self):
        # APIC
        pass

    def get_track_album(self):
        return self.data.get('TALB')
        # TALB
        pass

    # def get_album_name(self):
    #     pass

    def get_track_style(self):
        # TCON
        pass

    def get_track_copyright(self):
        # TCOP
        pass

    # def get_track_release_date(self):
    #     pass

    # def get_track_encoder(self):
    #     pass

    def get_track_publisher(self):
        # TPUB
        pass

    def get_track_number(self):
        return int(self.data.get('TRCK').text)
