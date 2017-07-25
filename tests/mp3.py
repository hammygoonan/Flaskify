from tests.base import BaseTestCase
from project.data.track import Track


class Mp3Tests(BaseTestCase):
    mp3_file_path = 'DJ Mustard/Ketchup - HotNewHipHop/08. DJ Mustard - LadyKilla Feat. Cocc Pi' +\
                    'stol Cree.mp3'
    mp3_file_path_with_year = 'David Bowie/David Bowie - The Rise And Fall Of Ziggy Stardust An' +\
                              'd The Spiders From Mars/09 - Ziggy Stardust.mp3'

    def test_mp3_get_title(self):
        mp3 = Track.get_details(self.mp3_file_path)
        self.assertEqual('LadyKilla Feat. Cocc Pistol Cree', mp3.get_title())

    def test_mp3_get_artists(self):
        mp3 = Track.get_details(self.mp3_file_path)
        self.assertEqual('DJ Mustard', mp3.get_artists())

    def test_mp3_get_album_artists(self):
        mp3 = Track.get_details(self.mp3_file_path)
        self.assertEqual('DJ Mustard', mp3.get_album_artists())

    def test_mp3_get_album_year(self):
        mp3 = Track.get_details(self.mp3_file_path_with_year)
        self.assertEqual(1972, mp3.get_album_year())

    def test_get_track_album(self):
        mp3 = Track.get_details(self.mp3_file_path)
        self.assertEqual('Ketchup', mp3.get_track_album())

    def test_get_track_number(self):
        mp3 = Track.get_details(self.mp3_file_path)
        self.assertEqual(8, mp3.get_track_number())

    def test_get_track_genre(self):
        mp3 = Track.get_details(self.mp3_file_path)
        self.assertEqual(['Hip-Hop'], mp3.get_track_genre())

    def test_get_track_publisher(self):
        mp3 = Track.get_details(self.mp3_file_path)
        self.assertEqual(['HotNewHipHop.com'], mp3.get_track_publisher())
