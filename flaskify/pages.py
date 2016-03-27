"""Pages routes."""

from flask import Blueprint, jsonify, render_template

from .models.library import Library

pages = Blueprint(
    'pages', __name__,
    template_folder='templates'
)


@pages.route('/')
def index():
    """Index page."""
    return render_template('index.html')


@pages.route("/songs")
def songs():
    """Song json."""
    library = Library()
    songs = [song.serialise() for song in library.songs]
    return jsonify({'songs': songs})


@pages.route("/albums")
def albums():
    """Album json."""
    library = Library()
    album = [album.serialise() for album in library.albums]
    return jsonify({'album': album})


@pages.route("/artists")
def artists():
    """Artist json."""
    library = Library()
    artist = [artist.serialise() for artist in library.artists]
    return jsonify({'artist': artist})
