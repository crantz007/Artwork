from unittest import TestCase

import database_config

database_config.database_path = 'artworks.db'

import artworkstore

from model import Artwork


class TestArtwork(TestCase):

    def test_create_artwork_default_available(self):
        aw = Artwork(artwork_name='Artwork name')
        self.assertFalse(aw.sold_artwork)

    def test_string(self):
        aw = Artwork(artwork_name='AAAA', artwork_price=13000, sold_artwork=True)
        self.assertIn('AAAA', str(aw))
        self.assertIn(13000, str(aw))
        self.assertIn('This artwork is sold', str(aw))

    def test_save_add_to_db(self):
        aw = Artwork(artwork_name='AAAA', artwork_price=10000, sold_artwork=True)
        aw.save()
        self.assertIsNone(aw.id)

        self.assertEqual(aw, artworkstore.get_artwork_by_id(aw.id))
        self.assertTrue(artworkstore.exact_match(aw))

    def test_save_update_changes_to_db(self):
        aw = Artwork(artwork_name='CCC', artwork_price=-10000, sold_artwork=True)
        aw.save()

        aw.artwork_name = 'EEE'
        aw.artwork_price = 1234567
        aw.sold_artwork = False

        aw.save()

        self.assertEqual(aw, artworkstore.get_artwork_by_id(aw.id))
        self.assertTrue(aw, artworkstore.exact_match(aw))
