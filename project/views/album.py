from flask import Blueprint
from flask import jsonify
from flask import abort
from flask import stream_with_context
from flask import Response
from project.models.album import Album
from mutagen.mp3 import MP3
import base64


album_blueprint = Blueprint('albums', __name__)


@album_blueprint.route('/<int:id>/')
def album(id):
    album = Album.query.get(id)
    if album:
        return jsonify(album.serialise())
    abort(404)


@album_blueprint.route('/')
def albums():
    albums = Album.query.all()
    return jsonify({'items': [album.serialise() for album in albums]})


@album_blueprint.route('/<int:id>/artwork')
def album_artwork(id):
    album = Album.query.get(id)
    if album:
        @stream_with_context
        def generate():
            mp3 = MP3(album.songs[0].path)
            art = mp3.get('APIC')
            print(art)
            yield base64.b64encode(art)
        return Response(generate())
    abort(404)

# /albums/<id>/songs
# /albums/<id>/artists
