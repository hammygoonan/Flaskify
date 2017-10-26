import pytest
from flaskify.data.track import Track

flac_file = 'Animal Collective/Merriweather Post Pavilion/01 - In the Flowers.flac'
flac_file_path_no_meta = 'Dr. Dre/Compton (2015)/01-dr._dre-intro.flac'


@pytest.mark.flac
def test_get_title(app):
    flac = Track.get_details(flac_file)
    assert 'In the Flowers' == flac.get_title()


@pytest.mark.flac
def test_get_artists(app):
    flac = Track.get_details(flac_file_path_no_meta)
    assert ['Dr. Dre'] == flac.get_artists()

    flac = Track.get_details(flac_file)
    assert ['Animal Collective'] == flac.get_artists()


@pytest.mark.flac
def test_get_album_artists(app):
    pass


@pytest.mark.flac
def test_get_album_year(app):
    flac = Track.get_details(flac_file_path_no_meta)
    assert 2015 == flac.get_album_year()


@pytest.mark.flac
def test_get_track_genre(app):
    flac = Track.get_details(flac_file_path_no_meta)
    assert ['Hip-Hop'] == flac.get_track_genre()

    flac = Track.get_details(flac_file)
    assert ['Indie'] == flac.get_track_genre()


@pytest.mark.flac
def test_get_track_number(app):
    flac = Track.get_details(flac_file)
    print(flac.__dict__)
    assert 1 == flac.get_track_number()

    flac = Track.get_details(flac_file)
    assert 1 == flac.get_track_number()
