from project.models.album import Album
from project.models.artist import Artist
from project.models.song import Song
from project.models.album_song import AlbumSong


def test_can_create_album_song(db):
    album = Album(title="The Rise And Fall Of Ziggy Stardust And The Spiders From Mars")
    artist = Artist(name="David Bowie")
    album.album_artists.append(artist)
    song = Song(title="Ziggy Stardust", path="/ziggy_stardust.mp3")
    song.artists.append(artist)
    album_song = AlbumSong()
    album_song.song = song
    album_song.album = album
    album_song.track_no = 9
    db.session.add(album)
    db.session.add(artist)
    db.session.add(song)
    db.session.add(album_song)
    db.session.commit()

    album_song = AlbumSong.query.first()
    print(album_song.album.__dict__)
    assert album_song.song.title == "Ziggy Stardust"
    assert album_song.album.title == "The Rise And Fall Of Ziggy Stardust And The Spiders From " +\
                                     "Mars"
    assert album_song.track_no == 9
