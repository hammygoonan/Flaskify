from flaskify.models.albums import Album
from flaskify.models.songs import Song
from flaskify.models.songs import AlbumSong


def test_can_access_album_songs(db):
    album = Album(title="This is an album")
    album.songs.append(Song(title="This is a song", path="path/to/song.mp3"))
    db.session.add(album)
    db.session.commit()

    album = Album.query.first()
    for song in album.songs:
        assert song.title == "This is a song"


def test_can_access_song_albums(db):
    song = Song(title="This is a song", path="path/to/song.mp3")
    song.albums.append(Album(title="This is an album"))
    db.session.add(song)
    db.session.commit()

    song = Song.query.first()
    for album in song.albums:
        assert album.title == "This is an album"


def test_can_add_track_number(db):
    song = Song(title="This is a song", path="path/to/song.mp3")
    album = Album(title="This is an album")
    album_song = AlbumSong(song=song, album=album, track_no=2)
    db.session.add(album_song)
    db.session.commit()

    assert song.song_albums[0].track_no == 2
    assert album.album_songs[0].track_no == 2
    assert song.song_albums[0].album.title == "This is an album"
    assert album.album_songs[0].song.title == "This is a song"
