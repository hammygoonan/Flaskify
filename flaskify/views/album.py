from flask import Blueprint
from flask import jsonify
from flask import abort
from flask import stream_with_context
from flask import Response
from flask import request
from flask import url_for
from flaskify.models.albums import Album
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
    page = request.args.get('p', 1)
    albums = Album.query.paginate(page=int(page), per_page=100)
    data = {
        'items': [album.serialise() for album in albums.items],
        'page': albums.page,
        'pages': albums.pages,
        'per_page': albums.per_page,
        'total': albums.total
    }
    if albums.has_next:
        data['next_page'] = url_for('albums.albums', p=albums.next_num)
    if albums.has_prev:
        data['next_page'] = url_for('albums.albums', p=albums.prev_num)
    return jsonify(data)


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
