from project import db
from tests.base import BaseTestCase
from project.models.album import Album


class AlbumTestCase(BaseTestCase):
    """Album Test Case."""
    def test_can_create_album(self):
        """Test can create Artist."""
        album = Album('Off the Wall', 'Michael Jackson')
        db.session.add(album)
        db.session.commit()

        assert album in db.session

    def test_can_read_album(self):
        """Test can read Album."""
        # album = Album('Off the Wall', 'Michael Jackson')
        # db.session.add(album)
        # db.session.commit()
        #
        # album_query = Album.query.filter_by(name='Off the Wall').first()
        # self.assertEqual('Michael Jackson', album_query.artist_name)
        pass

    def test_can_update_album(self):
        """Test can update Album."""
        pass

    def test_can_delete_album(self):
        """Test can delete Album."""
        pass
