from flaskify.data.track import Track


m4a_file_path = 'Amon Tobin/Dark Jovian/01 Dark Jovian.m4a'


def test_get_title(app):
    """Return MP4 track title."""
    mp4 = Track.get_details(m4a_file_path)
    assert 'Dark Jovian' == mp4.get_title()


def test_get_artists(app):
    """Return MP4 track artists."""
    mp4 = Track.get_details(m4a_file_path)
    assert ['Amon Tobin'] == mp4.get_artists()


def test_get_album_artists(app):
    """Return MP4 track album artists."""
    mp4 = Track.get_details(m4a_file_path)
    assert ['Amon Tobin'] == mp4.get_album_artists()


def test_get_album_year(app):
    """Return MP4 track year."""
    mp4 = Track.get_details(m4a_file_path)
    assert 2015 == mp4.get_album_year()


def test_get_track_album(app):
    """Return MP4 track album title."""
    mp4 = Track.get_details(m4a_file_path)
    assert 'Dark Jovian' == mp4.get_track_album()


def test_get_track_genre(app):
    """Return MP4 track genre."""
    mp4 = Track.get_details(m4a_file_path)
    assert ['Electronic'] == mp4.get_track_genre()


def test_get_track_copyright(app):
    """Return MP4 track copyright."""
    mp4 = Track.get_details(m4a_file_path)
    assert mp4.get_track_copyright() is None
