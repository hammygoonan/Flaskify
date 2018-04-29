from flask import Blueprint
from flask import jsonify
from flask import abort
from flask import request
from flask import url_for
from flask import send_from_directory
from flask import current_app

from flaskify.models.songs import Song


songs_blueprint = Blueprint('songs', __name__)


@songs_blueprint.route('/<int:id>/')
def song(id):
    song = Song.query.get(id)
    if song:
        return jsonify(song.serialise())
    abort(404)


@songs_blueprint.route('/')
def songs():
    page = request.args.get('p', 1)
    songs = Song.query.paginate(page=int(page), per_page=100)
    data = {
        'items': [artist.serialise() for artist in songs.items],
        'page': songs.page,
        'pages': songs.pages,
        'per_page': songs.per_page,
        'total': songs.total
    }
    if songs.has_next:
        data['next_page'] = url_for('songs.songs', p=songs.next_num)
    if songs.has_prev:
        data['next_page'] = url_for('songs.songs', p=songs.prev_num)
    return jsonify(data)


@songs_blueprint.route('/song_file/<path:filename>/')
def song_file(filename):
    # print(send_from_directory(current_app.config['MUSIC_DIR'][:-1], filename))
    return send_from_directory('static/music', filename)
