from time import sleep
from urllib.parse import quote

from project import db
from tests.base import BaseTestCase
from project.models.song import Song
from project.models.artist import Artist


class SongTestCase(BaseTestCase):
    """Song Test Case."""

    mp3_file_path = 'DJ Mustard/Ketchup - HotNewHipHop/08. DJ Mustard - La' +\
                    'dyKilla Feat. Cocc Pistol Cree.mp3'
    mp3_file_path_with_year = 'David Bowie/David Bowie - The Rise And Fall Of Ziggy Stardust An' +\
                              'd The Spiders From Mars/09 - Ziggy Stardust.mp3'
    m4a_file_path = 'Amon Tobin/Dark Jovian/01 Dark Jovian.m4a'
    flac_file_path = 'Dr. Dre/Compton (2015)/03-dr._dre-genocide_(feat._ken' +\
                     'drick_lamar_marsha_ambrosius_and_candice_pillay).flac'
    no_meta_file = 'Imperial Teen/What is Not to Love [1998]/04. Lipstic' +\
                   'k.flac'

    def test_can_create_song(self):
        """Test can create Song."""
        song = Song(self.mp3_file_path)
        db.session.add(song)
        db.session.commit()

        assert song in db.session

    def test_can_read_song(self):
        """Test can read Song."""
        pass

    def test_can_update_song(self):
        """Test can update Song."""
        pass

    def test_date_changed_after_update(self):
        """Test that the `last_updated` field is updated on save."""
        pass

    def test_can_delete_song(self):
        """Test can delete Song."""
        pass

    def test_song_serialise(self):
        """Test Song serialise method."""
        pass

    def test_get_file_type_flac(self):
        """Test `get_file_type` method."""
        song = Song(self.m4a_file_path)
        file_type = song.get_file_type()
        self.assertEqual('m4a', file_type)

    def test_get_file_type_mp3(self):
        """Test `get_file_type` method."""
        song = Song(self.mp3_file_path)
        file_type = song.get_file_type()
        self.assertEqual('mp3', file_type)

    def test_get_file_type_m3a(self):
        """Test `get_file_type` method."""
        song = Song(self.flac_file_path)
        file_type = song.get_file_type()
        self.assertEqual('flac', file_type)

    # def test_url_for(self):
    #     """Test `url_for` method."""
    #     song = Song(self.mp3_file_path)
    #     self.assertEqual(quote('/static/music/Music/' + self.mp3_file_path),
    #                      song.url_for)

    def test_no_metadata(self):
        pass

    def test_wav_file_format(self):
        pass

    def test_if_non_media_file(self):
        pass

    def test_track_title(self):
        song = Song(self.mp3_file_path)
        self.assertEqual('LadyKilla Feat. Cocc Pistol Cree',
                         song.get_track_title())

        song = Song(self.flac_file_path)
        self.assertEqual('Genocide (Feat. Kendrick Lamar, Marsha Ambrosius &'
                         ' Candice Pillay)', song.get_track_title())

        song = Song(self.m4a_file_path)
        self.assertEqual('Dark Jovian',
                         song.get_track_title())

        song = Song(self.no_meta_file)
        self.assertEqual('Lipstick',
                         song.get_track_title())

    def test_track_number(self):
        song = Song(self.mp3_file_path)
        self.assertEqual(8, song.get_track_number())

        song = Song(self.flac_file_path)
        self.assertEqual(3, song.get_track_number())

        song = Song(self.m4a_file_path)
        self.assertEqual(1, song.get_track_number())

        song = Song(self.no_meta_file)
        self.assertEqual(4, song.get_track_number())

        song = Song(self.no_meta_file)
        self.assertEqual(99, song.get_track_number(99))

    def test_track_year(self):
        song = Song(self.mp3_file_path)
        self.assertIsNone(song.get_track_year())

        song = Song(self.mp3_file_path_with_year)
        self.assertEqual(1972, song.get_track_year())

        song = Song(self.flac_file_path)
        self.assertIsNone(song.get_track_year())

        song = Song(self.m4a_file_path)
        self.assertIsNone(song.get_track_year())

        song = Song(self.no_meta_file)
        self.assertIsNone(song.get_track_year())

        song = Song(self.no_meta_file)
        self.assertEqual(1999, song.get_track_year(1999))

    def test_get_artists(self):
        song = Song(self.mp3_file_path)
        self.assertEqual('DJ Mustard', song.artists[0].name)

        song = Song(self.flac_file_path)
        self.assertEqual('Dr. Dre', song.artists[0].name)

        song = Song(self.m4a_file_path)
        self.assertEqual('Amon Tobin', song.artists[0].name)

        song = Song(self.no_meta_file)
        self.assertEqual('Imperial Teen', song.artists[0].name)

        song = Song(self.no_meta_file)
        song.artists = [Artist('Mystery Artist')]
        self.assertEqual('Mystery Artist', song.artists[0].name)

        song = Song(self.no_meta_file, artists="Mystery Artist")
        self.assertEqual('Mystery Artist', song.artists[0].name)

        song = Song(self.no_meta_file, artists=Artist("Mystery Artist"))
        self.assertEqual('Mystery Artist', song.artists[0].name)
