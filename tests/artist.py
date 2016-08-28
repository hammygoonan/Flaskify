from time import sleep

from project import db
from tests.base import BaseTestCase
from project.models.artist import Artist


class ArtistTestCase(BaseTestCase):
    """Artist Test Case."""
    def test_can_create_artist(self):
        """Test can create Artist."""
        album = Artist('Michael Jackson')
        db.session.add(album)
        db.session.commit()

        assert album in db.session

    def test_can_read_artist(self):
        """Test can read Artist."""
        album = Artist('Michael Jackson')
        db.session.add(album)
        db.session.commit()

        album_query = Artist.query.filter_by(name='Michael Jackson').first()
        self.assertEqual('Michael Jackson', album_query.name)

    def test_can_update_artist(self):
        """Test can update Artist."""
        album = Artist('Michael Jackson')
        db.session.add(album)
        db.session.commit()

        album = Artist.query.filter_by(name='Michael Jackson').first()
        album.name = "Phil Collins"
        db.session.add(album)
        db.session.commit()

        album = Artist.query.filter_by(name='Phil Collins').first()
        self.assertEqual('Phil Collins', album.name)

        album = Artist.query.filter_by(name='Michael Jackson').first()
        self.assertIsNone(album)

    def test_date_changed_after_update(self):
        """Test that the `last_updated` field is updated on save."""
        album = Artist('Michael Jackson')
        db.session.add(album)
        db.session.commit()
        created = album.last_updated

        sleep(1)
        album.name = "Phil Collins"
        db.session.commit()
        updated = album.last_updated
        self.assertNotEqual(created, updated)

    def test_can_delete_artist(self):
        """Test can delete Artist."""
        album = Artist('Michael Jackson')
        db.session.add(album)
        db.session.commit()

        album = Artist.query.filter_by(name='Michael Jackson').first()
        db.session.delete(album)
        db.session.commit()

        album = Artist.query.filter_by(name='Michael Jackson').first()
        self.assertIsNone(album)

    def test_artist_serialise(self):
        """Test Artist serialise method."""
        album = Artist('Michael Jackson')
        self.assertIsInstance(album.serialise(), dict)
