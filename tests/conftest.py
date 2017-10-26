import pytest
from flask.ctx import AppContext
from flaskify import create_app
from flaskify import db as _db


@pytest.fixture(scope='function')
def app(request):
    app = create_app('config.test')
    # Establish an application context before running the tests.
    ctx = AppContext(app)
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='function')
def db(app, request):
    """Function-wide test database."""
    _db.app = app
    _db.create_all()

    def teardown():
        _db.drop_all()

    request.addfinalizer(teardown)
    return _db
