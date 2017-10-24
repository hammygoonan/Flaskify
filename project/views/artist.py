from flask import Blueprint
from flask import jsonify
from flask import abort

from project.models.artist import Artist


artist_blueprint = Blueprint('artists', __name__)


@artist_blueprint.route('/<int:id>/')
def artist(id):
    artist = Artist.query.get(id)
    if artist:
        return jsonify(artist.serialise())
    abort(404)


@artist_blueprint.route('/')
def artists():
    artists = Artist.query.all()
    return jsonify({'items': [artist.serialise() for artist in artists]})

# /artists/<id>/songs
# /artists/<id>/albums
