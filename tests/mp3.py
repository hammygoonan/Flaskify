from tests.base import BaseTestCase
from project.data.track import Track


class Mp3Tests(BaseTestCase):
    mp3_file_path = 'DJ Mustard/Ketchup - HotNewHipHop/08. DJ Mustard - LadyKilla Feat. Cocc Pi' +\
                    'stol Cree.mp3'

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
        mp3 = Track.get_details(self.mp3_file_path)
        self.assertEqual(2015, mp3.get_album_year())

    def test_get_track_album(self):
        mp3 = Track.get_details(self.mp3_file_path)
        self.assertEqual(8, mp3.get_track_album())

    def test_get_track_number(self):
        mp3 = Track.get_details(self.mp3_file_path)
        self.assertEqual(8, mp3.get_track_number())
