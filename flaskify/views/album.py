"""Album views.

:copyright: (c) 2018 Hammy Goonan
"""
import io
from flask import Blueprint
from flask import jsonify
from flask import abort
from flask import request
from flask import url_for
from flask import send_file
from flaskify.models.albums import Album


album_blueprint = Blueprint('albums', __name__)


@album_blueprint.route('/<int:id>/')
def album(id):
    """Return album resource."""
    album = Album.query.get(id)
    if album:
        return jsonify(album.serialise())
    abort(404)


@album_blueprint.route('/')
def albums():
    """Return collection of albums."""
    page = request.args.get('p', 1)
    albums = Album.query.order_by('title').paginate(page=int(page), per_page=50)
    data = {
        'collection': [album.serialise() for album in albums.items],
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


@album_blueprint.route('/<int:id>/artwork/')
def album_artwork(id):
    """Return album artwork."""
    album = Album.query.get(id)
    if album and album.album_art:
        return send_file(io.BytesIO(album.album_art),
                         attachment_filename='album.jpeg',
                         mimetype='image/jpeg')

    abort(404)
