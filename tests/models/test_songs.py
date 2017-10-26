import pytest
from time import sleep
import datetime
from flask import url_for
from flaskify.models.songs import Song
from flaskify.models.artists import Artist
from flaskify.models.albums import Album


def test_song_can_save_song(db):
    song = Song(title="test title", path="/song_path.mp3")
    db.session.add(song)
    db.session.commit()

    song = Song.query.first()
    assert "test title" == song.title
    assert "/song_path.mp3" == song.path


def test_song_requires_title(db):
    song = Song(path="/song_path.mp3")
    db.session.add(song)
    with pytest.raises(Exception):
        db.session.commit()


def test_song_requires_path(db):
    song = Song(title="test title")
    db.session.add(song)
    with pytest.raises(Exception):
        db.session.commit()


def test_datetime_defults_to_current_time(db):
    song = Song(title="test title", path="/song_path.mp3")
    db.session.add(song)
    db.session.commit()

    now = datetime.datetime.utcnow()
    song = Song.query.first()

    assert now.year == song.last_updated.year
    assert now.month == song.last_updated.month
    assert now.day == song.last_updated.day
    assert now.hour == song.last_updated.hour
    assert now.minute == song.last_updated.minute
    assert now.second == song.last_updated.second


def test_update_listener(db):
    """Test last_updated event is working."""
    song = Song(title="test name", path="/testpath.mp3")
    db.session.add(song)
    db.session.commit()

    now = datetime.datetime.utcnow()

    sleep(1)
    song.title = "One Second later"
    db.session.commit()

    assert now.second + 1 == song.last_updated.second


def test_path_is_unique(db):
    song = Song(title="test name", path="/testpath.mp3")
    db.session.add(song)
    db.session.commit()

    song = Song(title="test other name", path="/testpath.mp3")
    db.session.add(song)

    with pytest.raises(Exception):
        db.session.commit()


def test_can_add_multiple_artists_to_a_song(db):
    song = Song(title="test name", path="/testpath.mp3")
    song.artists.append(Artist(name="Artist One"))
    song.artists.append(Artist(name="Artist Two"))
    db.session.add(song)
    db.session.commit()

    song = Song.query.first()

    for artist in song.artists:
        assert artist.name in ["Artist One", "Artist Two"]


def test_serialise(db):
    song = Song(title="Song title", path="song/path.mp3")
    song.artists.append(Artist(name="Artist name"))
    song.albums.append(Album(title="Album title"))
    db.session.add(song)
    db.session.commit()

    assert {
        'id': song.id,
        'title': song.title,
        'last_updated': song.last_updated,
        'url': url_for('songs.song', id=song.id),
        'artists': [
            {
                'id': artist.id,
                'name': artist.name,
                'url': url_for('artists.artist', id=song.id)
            }
            for artist in song.artists
        ],
        'albums': [
            {
                'id': album.id,
                'title': album.title,
                'url': url_for('albums.album', id=song.id)
            }
            for album in song.albums
        ]
    } == song.serialise()
