#!/usr/bin/env python
"""
Basic CLI interface for application.

To run application simply call manage.py followed by single argument which corresponds to
function name
"""

import sys
from flaskify import create_app
from flaskify import db


def runserver():
    """Runs development server."""
    app = create_app('config.development')
    app.run()


def create_database():
    """Create empty database."""
    from flaskify.models import albums, artists, songs  # noqa
    app = create_app('config.development')
    with app.app_context():
        db.create_all()


def scan_dir():
    from flaskify.utils.scanner import scan_dir
    app = create_app('config.development')
    with app.app_context():
        scan_dir()


if __name__ == "__main__":
    manage = sys.modules[__name__]
    if hasattr(manage, sys.argv[1]):
        result = getattr(manage, sys.argv[1])()
    else:
        raise ValueError('This operation does not exist')
