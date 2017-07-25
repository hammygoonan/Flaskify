from tests.base import BaseTestCase
from project.data.track import Track


class Mp4Tests(BaseTestCase):
    m4a_file_path = 'Amon Tobin/Dark Jovian/01 Dark Jovian.m4a'

    def test_get_title(self):
        mp4 = Track.get_details(self.m4a_file_path)
        self.assertEqual(['Dark Jovian'], mp4.get_title())

    def test_get_artists(self):
        mp4 = Track.get_details(self.m4a_file_path)
        self.assertEqual(['Amon Tobin'], mp4.get_artists())

    def test_get_album_artists(self):
        mp4 = Track.get_details(self.m4a_file_path)
        self.assertEqual(['Amon Tobin'], mp4.get_album_artists())

    def test_get_album_year(self):
        mp4 = Track.get_details(self.m4a_file_path)
        self.assertEqual(2015, mp4.get_album_year())

    def test_get_track_album(self):
        mp4 = Track.get_details(self.m4a_file_path)
        self.assertEqual(['Dark Jovian'], mp4.get_track_album())

    def test_get_track_genre(self):
        mp4 = Track.get_details(self.m4a_file_path)
        self.assertEqual(['Electronic'], mp4.get_track_genre())

    def test_get_track_copyright(self):
        mp4 = Track.get_details(self.m4a_file_path)
        self.assertEqual(None, mp4.get_track_copyright())
