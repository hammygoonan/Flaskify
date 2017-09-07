from time import sleep

from project.models.album import Album
from project.models.artist import Artist


def test_can_create_album(db):
    """Test can create Artist."""
    artist = Artist(name='Michael Jackson')
    album = Album(title='Off the Wall', album_artists=[artist])
    db.session.add(album)
    db.session.commit()

    assert album in db.session


def test_can_read_album(db):
    """Test can read Album."""
    artist = Artist(name='Michael Jackson')
    album = Album(title='Off the Wall', album_artists=[artist])
    db.session.add(album)
    db.session.commit()

    album_query = Album.query.filter_by(title='Off the Wall').first()
    assert 'Michael Jackson' == album_query.album_artists[0].name


def test_can_update_album(db):
    """Test can update Album."""
    album = Album(title='Off the Wall')
    db.session.add(album)
    db.session.commit()

    album_query = Album.query.filter_by(title='Off the Wall').first()
    album_query.title = 'Coming in the air tonight'
    db.session.add(album_query)
    db.session.commit()

    album_query = Album.query.filter_by(title='Coming in the air tonight').first()
    assert 'Coming in the air tonight' == album_query.title

    album_query = Album.query.filter_by(title='Off the Wall').first()
    assert album_query is None


def test_can_delete_album(db):
    """Test can delete Album."""
    album = Album(title='Off the Wall')
    db.session.add(album)
    db.session.commit()

    album = Album.query.filter_by(title='Off the Wall').first()
    db.session.delete(album)
    db.session.commit()

    album = Artist.query.filter_by(name='Off the Wall').first()
    assert album is None


def test_date_changed_after_update(db):
    """Test that the `last_updated` field is updated on save."""
    album = Album(title='Off the Wall')
    db.session.add(album)
    db.session.commit()
    created = album.last_updated

    sleep(1)
    album.title = "POff the Wall"
    db.session.commit()
    updated = album.last_updated
    assert created != updated


def test_album_serialise(db):
    artist = Artist(name='Michael Jackson')
    album = Album(title='Off the Wall', album_artists=[artist])
    assert isinstance(album.serialise(), dict)
    assert isinstance(album.serialise()['album_artists'], list)
