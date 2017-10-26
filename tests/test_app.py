from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def test_create_app_returns_flask_instance():
    """Test `create_app` function returns Flask instance."""
    from flaskify import create_app
    assert isinstance(create_app(), Flask)


def test_create_app_initiates_database_connection():
    """Test `create_app` function returns Flask instance."""
    import flaskify
    assert isinstance(flaskify.db, SQLAlchemy)
    assert isinstance(flaskify.db.app, Flask)
