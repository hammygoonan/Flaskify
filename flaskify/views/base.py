from flask import Blueprint
from flask import render_template

base_blueprint = Blueprint('base', __name__)


@base_blueprint.route('/')
def index():
    return render_template('hello.html')
