#!/usr/bin/env python
"""
Basic CLI interface for application.

To run application simply call manage.py followed by single argument which corresponds to
function name
"""

import sys
import unittest
from project import create_app
from project import db


def runserver():
    """Runs development server."""
    app = create_app('config.Development')
    app.run()


def test():
    """Runs test suite."""
    pattern = '*.py'
    if len(sys.argv) > 2:
        pattern = sys.argv[2]
    tests = unittest.TestLoader().discover('tests', pattern=pattern)
    unittest.TextTestRunner(verbosity=1).run(tests)


def create_database():
    """Create empty database."""
    from project.models import album_song, album, artist, song  # noqa
    app = create_app('config.Development')
    with app.app_context():
        db.create_all()


# def update_library():
#     from project.models.library import Library
#     app = create_app('config.Development')
#     with app.app_context():
#         Library()


def scan_dir():
    from project.utils.scanner import scan_dir
    app = create_app('config.Development')
    with app.app_context():
        scan_dir()


if __name__ == "__main__":
    manage = sys.modules[__name__]
    if hasattr(manage, sys.argv[1]):
        result = getattr(manage, sys.argv[1])()
    else:
        raise ValueError('This operation does not exist')
