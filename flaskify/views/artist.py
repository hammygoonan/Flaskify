from flask import Blueprint
from flask import jsonify
from flask import abort
from flask import request
from flask import url_for

from flaskify.models.artists import Artist


artist_blueprint = Blueprint('artists', __name__)


@artist_blueprint.route('/<int:id>/')
def artist(id):
    artist = Artist.query.get(id)
    if artist:
        return jsonify(artist.serialise())
    abort(404)


@artist_blueprint.route('/')
def artists():
    page = request.args.get('p', 1)
    artists = Artist.query.paginate(page=int(page), per_page=100)
    data = {
        'items': [artist.serialise() for artist in artists.items],
        'page': artists.page,
        'pages': artists.pages,
        'per_page': artists.per_page,
        'total': artists.total
    }
    if artists.has_next:
        data['next_page'] = url_for('artists.artists', p=artists.next_num)
    if artists.has_prev:
        data['next_page'] = url_for('artists.artists', p=artists.prev_num)
    return jsonify(data)

# /artists/<id>/songs
# /artists/<id>/albums
