from datetime import datetime
from mutagen.mp4 import MP4
from .track import Track


class Mp4(Track):
    def __init__(self, path):
        super().__init__(path)
        self.data = self.get_mp4(self.path)

    def get_mp4(self, path):
        """Return MP3 object.

        :param path: String, filename relative to MEDIA_DIR.
        :return: :class:`MP4 <MP4>`
        """
        return MP4(self.get_file_path())

    def get_title(self):
        return self.data.get('©nam')

    def get_artists(self):
        return self.data.get('©ART')

    def get_album_artists(self):
        return self.data.get('aART')

    def get_album_year(self):
        date = datetime.strptime(self.data.get('©day')[0], '%Y-%m-%dT%H:%M:%SZ')
        return int(date.strftime('%Y'))

    def get_album_pic(self):
        return self.data.get('covr')

    def get_track_album(self):
        return self.data.get('©alb')

    def get_track_genre(self):
        return self.data.get('©gen')

    def get_track_copyright(self):
        return self.data.get('cprt')

    def get_track_publisher(self):
        return None

    def get_track_number(self):
        return self.data.get('trkn')
