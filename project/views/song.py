from flask import Blueprint
from flask import jsonify
from flask import abort

from project.models.song import Song


songs_blueprint = Blueprint('songs', __name__)


@songs_blueprint.route('/<int:id>/')
def song(id):
    song = Song.query.get(id)
    if song:
        return jsonify(song.serialise())
    abort(404)


@songs_blueprint.route('/')
def songs():
    songs = Song.query.all()
    return jsonify({'items': [song.serialise() for song in songs]})

# /songs/<id>/artists
# /songs/<id>/albums
# pagination
