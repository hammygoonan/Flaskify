from flask_testing import TestCase

from project import create_app
from project import db


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app('config.Test')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        """Tear down tests."""
        db.session.remove()
        db.drop_all()
