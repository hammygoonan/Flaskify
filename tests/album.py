from time import sleep

from project import db
from tests.base import BaseTestCase
from project.models.album import Album
from project.models.artist import Artist


class AlbumTestCase(BaseTestCase):
    """Album Test Case."""
    def test_can_create_album(self):
        """Test can create Artist."""
        artist = Artist('Michael Jackson')
        album = Album('Off the Wall', album_artists=[artist])
        db.session.add(album)
        db.session.commit()

        assert album in db.session

    def test_can_read_album(self):
        """Test can read Album."""
        artist = Artist('Michael Jackson')
        album = Album('Off the Wall', album_artists=[artist])
        db.session.add(album)
        db.session.commit()

        album_query = Album.query.filter_by(name='Off the Wall').first()
        self.assertEqual('Michael Jackson', album_query.album_artists[0].name)

    def test_can_update_album(self):
        """Test can update Album."""
        album = Album('Off the Wall')
        db.session.add(album)
        db.session.commit()

        album_query = Album.query.filter_by(name='Off the Wall').first()
        album_query.name = 'Coming in the air tonight'
        db.session.add(album_query)
        db.session.commit()

        album_query = Album.query.filter_by(name='Coming in the air tonight').first()
        self.assertEqual('Coming in the air tonight', album_query.name)

        album_query = Album.query.filter_by(name='Off the Wall').first()
        self.assertIsNone(album_query)

    def test_can_delete_album(self):
        """Test can delete Album."""
        album = Album('Off the Wall')
        db.session.add(album)
        db.session.commit()

        album = Album.query.filter_by(name='Off the Wall').first()
        db.session.delete(album)
        db.session.commit()

        album = Artist.query.filter_by(name='Off the Wall').first()
        self.assertIsNone(album)

    def test_date_changed_after_update(self):
        """Test that the `last_updated` field is updated on save."""
        album = Artist('Off the Wall')
        db.session.add(album)
        db.session.commit()
        created = album.last_updated

        sleep(1)
        album.name = "POff the Wall"
        db.session.commit()
        updated = album.last_updated
        self.assertNotEqual(created, updated)

    def test_album_serialise(self):
        artist = Artist('Michael Jackson')
        album = Album('Off the Wall', album_artists=[artist])
        self.assertIsInstance(album.serialise(), dict)
        self.assertIsInstance(album.serialise()['album_artists'], list)
