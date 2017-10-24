# from tests.base import BaseTestCase
from project.models.song import Song
# from project.models.artist import Artist


# class TestSongCase():
#     """Song Test Case."""
#
#     mp3_file_path = 'DJ Mustard/Ketchup - HotNewHipHop/08. DJ Mustard - La' +\
#                     'dyKilla Feat. Cocc Pistol Cree.mp3'
mp3_file_path_with_year = 'David Bowie/David Bowie - The Rise And Fall Of Ziggy Stardust An' +\
                              'd The Spiders From Mars/09 - Ziggy Stardust.mp3'
#     m4a_file_path = 'Amon Tobin/Dark Jovian/01 Dark Jovian.m4a'
#     flac_file_path = 'Dr. Dre/Compton (2015)/03-dr._dre-genocide_(feat._ken' +\
#                      'drick_lamar_marsha_ambrosius_and_candice_pillay).flac'
#     no_meta_file = 'Imperial Teen/What is Not to Love [1998]/04. Lipstic' +\
#                    'k.flac'


def test_can_create_song_creation(db):
    song = Song(title='Ziggy Stardust', path=mp3_file_path_with_year)
    db.session.add(song)
    db.session.commit()

    song = Song.query.filter_by(title='Ziggy Stardust').all()
    assert len(song) == 1
    assert song[0].title == 'Ziggy Stardust'


def test_can_access_artists(test_mp3):
    song = Song.query.first()
    for artist in song.artists:
        assert artist.name == "DJ Mustard"
