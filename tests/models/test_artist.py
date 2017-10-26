import pytest
from time import sleep
import datetime
from flaskify.models.artists import Artist
from flaskify.models.albums import Album
from flaskify.models.songs import Song


def test_can_save_album(db):
    artist = Artist(name="test name")
    db.session.add(artist)
    db.session.commit()

    artist = Artist.query.first()
    assert "test name" == artist.name


def test_album_requires_title(db):
    artist = Artist()
    db.session.add(artist)
    with pytest.raises(Exception):
        db.session.commit()

    artist = Artist(last_updated=datetime.datetime.utcnow())
    db.session.add(artist)
    with pytest.raises(Exception):
        db.session.commit()


def test_datetime_defults_to_current_time(db):
    artist = Artist(name="test name")
    db.session.add(artist)
    db.session.commit()

    now = datetime.datetime.utcnow()
    artist = Artist.query.first()

    assert now.year == artist.last_updated.year
    assert now.month == artist.last_updated.month
    assert now.day == artist.last_updated.day
    assert now.hour == artist.last_updated.hour
    assert now.minute == artist.last_updated.minute
    assert now.second == artist.last_updated.second


def test_update_listener(db):
    """Test last_updated event is working."""
    artist = Artist(name="test name")
    db.session.add(artist)
    db.session.commit()

    now = datetime.datetime.utcnow()

    sleep(1)
    artist.name = "One Second later"
    db.session.commit()

    assert now.second + 1 == artist.last_updated.second


def test_can_add_albums_to_artists(db):
    """Test can add multiple artists to album."""
    artist = Artist(name="test artist")
    artist.albums.append(Album(title="test title"))
    db.session.add(artist)
    db.session.commit()

    artist = Artist.query.first()
    album = Album.query.first()

    assert "test title" == album.title
    assert "test artist" == artist.name
    assert "test artist" == album.artists[0].name
    assert "test title" == artist.albums[0].title


def test_can_add_multiple_songs_to_artist(db):
    artist = Artist(name="test artist")
    artist.songs.append(Song(title="Song One", path="song_1.mp3"))
    artist.songs.append(Song(title="Song Two", path="song_2.mp3"))
    db.session.add(artist)
    db.session.commit()

    artist = Artist.query.first()
    for song in artist.songs:
        assert song.title in ["Song One", "Song Two"]
