from tests.base import BaseTestCase
from project.data.track import Track
from project.data.mp3 import Mp3
from project.data.mp4 import Mp4
from project.data.m4a import M4a
from project.data.flac import Flac


class TrackTests(BaseTestCase):

    def test_factory_returns_mp3_class(self):
        mp3_file_path = 'DJ Mustard/Ketchup - HotNewHipHop/08. DJ Mustard - LadyKilla Feat. Coc' +\
                        'c Pistol Cree.mp3'
        mp3 = Track.get_details(mp3_file_path)
        self.assertIsInstance(mp3, Mp3)

    def test_factory_returns_flac_class(self):
        flac = Track.get_details('test.flac')
        self.assertIsInstance(flac, Flac)

    def test_factory_returns_m4a_class(self):
        m4a = Track.get_details('test.m4a')
        self.assertIsInstance(m4a, M4a)

    def test_factory_returns_mp4_class(self):
        mp3 = Track.get_details('test.mp4')
        self.assertIsInstance(mp3, Mp4)

    def test_error_if_filetype_not_supported(self):
        with self.assertRaises(Exception):
            Track.get_details('test.abc')
