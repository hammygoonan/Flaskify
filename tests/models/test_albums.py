import pytest
import datetime
from time import sleep
from flaskify.models.albums import Album
from flaskify.models.artists import Artist


def test_can_save_album(db):
    album = Album(title="test title")
    db.session.add(album)
    db.session.commit()

    album = Album.query.first()
    assert "test title" == album.title


def test_album_requires_title(db):
    album = Album()
    db.session.add(album)
    with pytest.raises(Exception):
        db.session.commit()

    album = Album(last_updated=datetime.datetime.utcnow())
    db.session.add(album)
    with pytest.raises(Exception):
        db.session.commit()


def test_datetime_defults_to_current_time(db):
    album = Album(title="test title")
    db.session.add(album)
    db.session.commit()

    now = datetime.datetime.utcnow()
    album = Album.query.first()

    assert now.year == album.last_updated.year
    assert now.month == album.last_updated.month
    assert now.day == album.last_updated.day
    assert now.hour == album.last_updated.hour
    assert now.minute == album.last_updated.minute
    assert now.second == album.last_updated.second


def test_update_listener(db):
    """Test last_updated event is working."""
    album = Album(title="test title")
    db.session.add(album)
    db.session.commit()

    now = datetime.datetime.utcnow()

    sleep(1)
    album.title = "One Second later"
    db.session.commit()

    assert now.second + 1 == album.last_updated.second


def test_can_add_artists_to_albums(db):
    """Test can add multiple artists to album."""
    album = Album(title="test title")
    album.artists.append(Artist(name="test artist"))
    db.session.add(album)
    db.session.commit()

    artist = Artist.query.first()
    album = Album.query.first()

    assert "test title" == album.title
    assert "test artist" == artist.name
    assert "test artist" == album.artists[0].name
    assert "test title" == artist.albums[0].title
