from time import sleep
from project.models.artist import Artist


def test_can_create_artist(db):
    """Test can create Artist."""
    artist = Artist(name='Michael Jackson')
    db.session.add(artist)
    db.session.commit()

    assert artist in db.session


def test_can_read_artist(db):
    """Test can read Artist."""
    artist = Artist(name='Michael Jackson')
    db.session.add(artist)
    db.session.commit()

    artist_query = Artist.query.filter_by(name='Michael Jackson').first()
    assert 'Michael Jackson' == artist_query.name


def test_can_update_artist(db):
    """Test can update Artist."""
    artist = Artist(name='Michael Jackson')
    db.session.add(artist)
    db.session.commit()

    artist = Artist.query.filter_by(name='Michael Jackson').first()
    artist.name = "Phil Collins"
    db.session.add(artist)
    db.session.commit()

    artist = Artist.query.filter_by(name='Phil Collins').first()
    assert 'Phil Collins' == artist.name

    artist = Artist.query.filter_by(name='Michael Jackson').first()
    assert artist is None


def test_date_changed_after_update(db):
    """Test that the `last_updated` field is updated on save."""
    artist = Artist(name='Michael Jackson')
    db.session.add(artist)
    db.session.commit()
    created = artist.last_updated

    sleep(1)
    artist.name = "Phil Collins"
    db.session.commit()
    updated = artist.last_updated
    assert created != updated


def test_can_delete_artist(db):
    """Test can delete Artist."""
    artist = Artist(name='Michael Jackson')
    db.session.add(artist)
    db.session.commit()

    artist = Artist.query.filter_by(name='Michael Jackson').first()
    db.session.delete(artist)
    db.session.commit()

    artist = Artist.query.filter_by(name='Michael Jackson').first()
    assert artist is None


def test_artist_serialise(db):
    """Test Artist serialise method."""
    artist = Artist(name='Michael Jackson')
    assert isinstance(artist.serialise(), dict)
