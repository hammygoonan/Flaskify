import pytest
from flaskify.data.track import Track

ogg_file = 'Fugazi/13 songs/fugazi - 01 - waiting room.ogg'


@pytest.mark.ogg
def test_get_title(app):
    ogg = Track.get_details(ogg_file)
    assert 'Waiting Room' == ogg.get_title()


@pytest.mark.ogg
def test_get_artists(app):
    ogg = Track.get_details(ogg_file)
    assert ['Fugazi'] == ogg.get_artists()


@pytest.mark.ogg
def test_get_album_artists(app):
    ogg = Track.get_details(ogg_file)
    assert ['Fugazi'] == ogg.get_album_artists()


@pytest.mark.ogg
def test_get_track_album(app):
    ogg = Track.get_details(ogg_file)
    assert '13 Songs' == ogg.get_track_album()


@pytest.mark.ogg
def test_get_album_year(app):
    ogg = Track.get_details(ogg_file)
    assert 1990 == ogg.get_album_year()


@pytest.mark.ogg
def test_get_track_genre(app):
    ogg = Track.get_details(ogg_file)
    assert ['Rock'] == ogg.get_track_genre()


@pytest.mark.ogg
def test_get_track_number(app):
    ogg = Track.get_details(ogg_file)
    assert 1 == ogg.get_track_number()
