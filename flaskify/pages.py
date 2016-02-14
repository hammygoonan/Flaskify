from flask import Blueprint, jsonify

from .models.library import Library

pages = Blueprint(
    'pages', __name__,
    template_folder='templates'
)


@pages.route("/songs")
def songs():
    """Index page."""
    library = Library()
    print(library.songs[0].id)
    songs = [song.serialise() for song in library.songs]
    return jsonify({'songs': songs})


@pages.route("/albums")
def albums():
    """Index page."""
    library = Library()
    album = [album.serialise() for album in library.albums]
    return jsonify({'album': album})


@pages.route("/artists")
def artists():
    """Index page."""
    library = Library()
    artist = [artist.serialise() for artist in library.artists]
    return jsonify({'artist': artist})
