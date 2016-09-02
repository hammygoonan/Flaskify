from time import sleep

from project import db
from tests.base import BaseTestCase
from project.models.artist import Artist


class ArtistTestCase(BaseTestCase):
    """Artist Test Case."""
    def test_can_create_artist(self):
        """Test can create Artist."""
        artist = Artist('Michael Jackson')
        db.session.add(artist)
        db.session.commit()

        assert artist in db.session

    def test_can_read_artist(self):
        """Test can read Artist."""
        artist = Artist('Michael Jackson')
        db.session.add(artist)
        db.session.commit()

        artist_query = Artist.query.filter_by(name='Michael Jackson').first()
        self.assertEqual('Michael Jackson', artist_query.name)

    def test_can_update_artist(self):
        """Test can update Artist."""
        artist = Artist('Michael Jackson')
        db.session.add(artist)
        db.session.commit()

        artist = Artist.query.filter_by(name='Michael Jackson').first()
        artist.name = "Phil Collins"
        db.session.add(artist)
        db.session.commit()

        artist = Artist.query.filter_by(name='Phil Collins').first()
        self.assertEqual('Phil Collins', artist.name)

        artist = Artist.query.filter_by(name='Michael Jackson').first()
        self.assertIsNone(artist)

    def test_date_changed_after_update(self):
        """Test that the `last_updated` field is updated on save."""
        artist = Artist('Michael Jackson')
        db.session.add(artist)
        db.session.commit()
        created = artist.last_updated

        sleep(1)
        artist.name = "Phil Collins"
        db.session.commit()
        updated = artist.last_updated
        self.assertNotEqual(created, updated)

    def test_can_delete_artist(self):
        """Test can delete Artist."""
        artist = Artist('Michael Jackson')
        db.session.add(artist)
        db.session.commit()

        artist = Artist.query.filter_by(name='Michael Jackson').first()
        db.session.delete(artist)
        db.session.commit()

        artist = Artist.query.filter_by(name='Michael Jackson').first()
        self.assertIsNone(artist)

    def test_artist_serialise(self):
        """Test Artist serialise method."""
        artist = Artist('Michael Jackson')
        self.assertIsInstance(artist.serialise(), dict)
