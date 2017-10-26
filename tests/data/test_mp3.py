import pytest
from flaskify.data.track import Track


mp3_file_path = 'DJ Mustard/Ketchup - HotNewHipHop/08. DJ Mustard - LadyKilla Feat. Cocc Pi' +\
                'stol Cree.mp3'
mp3_file_path_with_year = 'David Bowie/David Bowie - The Rise And Fall Of Ziggy Stardust An' +\
                          'd The Spiders From Mars/09 - Ziggy Stardust.mp3'
mp3_without_data = 'A$AP Rocky/LiveLoveA$AP (2011)/16 Asap Rocky - Out Of This World ' +\
                   '[Prod. By The Olympicks].mp3'


@pytest.mark.mp3
def test_mp3_get_title(app):
    mp3 = Track.get_details(mp3_file_path)
    assert 'LadyKilla Feat. Cocc Pistol Cree' == mp3.get_title()


# @pytest.mark.mp3
# def test_mp3_get_title_without_data(app):
#     mp3 = Track.get_details(mp3_without_data)
#     assert '' == mp3.get_title()


def test_mp3_get_artists(app):
    mp3 = Track.get_details(mp3_file_path)
    assert ['DJ Mustard'] == mp3.get_artists()


def test_mp3_get_album_artists(app):
    mp3 = Track.get_details(mp3_file_path)
    assert ['DJ Mustard'] == mp3.get_album_artists()


def test_mp3_get_album_year(app):
    mp3 = Track.get_details(mp3_file_path_with_year)
    assert 1972 == mp3.get_album_year()


def test_get_track_album(app):
    mp3 = Track.get_details(mp3_file_path)
    assert 'Ketchup' == mp3.get_track_album()


def test_get_track_number(app):
    mp3 = Track.get_details(mp3_file_path)
    assert 8 == mp3.get_track_number()


def test_get_track_genre(app):
    mp3 = Track.get_details(mp3_file_path)
    assert ['Hip-Hop'] == mp3.get_track_genre()


def test_get_track_publisher(app):
    mp3 = Track.get_details(mp3_file_path)
    assert ['HotNewHipHop.com'] == mp3.get_track_publisher()


def test_non_number_track_number(app):
    track = 'DJ Shadow/2007 - DJ Shadow - James Brown - 50th Anniversary (Fatboy Slim)/A James ' +\
            'Brown - Happy Birthday from DJ Shadow.mp3'
    mp3 = Track.get_details(track)
    assert 'A' == mp3.get_track_number()


def test_get_track_no_number(app):
    track = '/Users/hammygoonan/Music/DJ Shadow/2007 - DJ Shadow - Break Set/fraykerbreaks ' +\
            'presents -the dj shadow breaks set.mp3'
    mp3 = Track.get_details(track)
    assert mp3.get_track_number() is None
