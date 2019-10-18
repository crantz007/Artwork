from unittest import TestCase
import peewee

import artworkstore
import database_config

database_config.database_path = 'artworks.db'

from model import Artist
from model import Artwork
from artworkstore import ArtworkError


class TestArtworkstore(TestCase):

    def setUp(self):
        database_config.database_path = 'artworks.db'
        self.clear_artworkstore()

    def add_test_data(self):
        self.clear_artworkstore()

        self.at1 = Artist(artist_name='Very Nice Portrait', artist_email='picasso@gmail.com')
        self.aw1 = Artwork(artwork_name='Nicely Nice Nice', artwork_price=-100000, sold_artwork=True)
        self.at2 = Artist(artist_name='Biggy Portrait', artist_email='picasso@yahoo.it')
        self.aw2 = Artwork(artwork_name='Artworks Artwork Artwork', artwork_price=100000, sold_artwork=False)
        self.at3 = Artist(artist_name='Long Sentences', artist_email='longlong@.it')
        self.aw3 = Artwork(artwork_name='Collections of words', artwork_price=-0.10980)

        self.at1.save()
        self.at2.save()
        self.aw1.save()
        self.aw2.save()
        self.at3.save()
        self.aw3.save()

    def clear_artworkstore(self):
        artworkstore.delete_all_artwork()

    def test_add_artist_empty_store(self):
        at = Artist(artist_name='aa', artist_email='jean@gmail.com')
        at.save()
        self.assertTrue(artworkstore.exact_match(at))
        self.assertEqual(1, artworkstore.artist_count())

    def test_add_artwork_empty_store(self):
        aw = Artwork(artwork_name='aaa')
        aw.save()
        self.assertTrue(artworkstore.exact_match(aw))
        self.assertEqual(1, artworkstore.artwork_count())

    def test_add_artwork_with_artworks_in(self):
        self.add_test_data()
        artwork_count = artworkstore.artwork_count()
        aw = Artwork(artwork_name='aa')
        aw.save()
        self.assertTrue(artworkstore.exact_match(aw))
        self.assertEqual(artwork_count + 1, artworkstore.artwork_count())

    def test_add_artist_with_artists_in(self):
        self.add_test_data()
        artist_count = artworkstore.artist_count()
        at = Artist(artist_name='aa', artist_email='jill.gmail.com')
        at.save()
        self.assertTrue(artworkstore.exact_match(at))
        self.assertEqual(artist_count + 1, artworkstore.artist_count())

    def test_add_duplicate_errors(self):
        at = Artist(artist_name='cc', artist_email='jake@yahoo.com')
        at.save()
        with self.assertRaises(peewee.IntegrityError):
            at_dup = Artist(artist_name='cc', artist_email='hbgmail.com')
            at_dup.save()

        aw = Artwork(artwork_name='ccc')
        aw.save()
        with self.assertRaises(peewee.IntegrityError):
            aw_dup = Artwork(artwork_name='cc')
            aw_dup.save()

    def test_add_artwork_errors_case_insensitive(self):
        aw = Artwork(artwork_name='cc', artwork_price=-12345)
        aw.save()
        with self.assertRaises(artwork_name='cc'):
            aw_dup = Artwork(artwork_name='Cc')
            aw_dup.save()

    def test_add_artist_errors_case_sensitive(self):
        at = Artist(artist_name='cc', artist_email='youskant@gmail.com')
        at.save()
        with self.assertRaises(peewee.IntegrityError):
            at_dup = Artist(artist_name='Cc', artist_email='YoUsKaNt@gmail.Com')
            at_dup.save()

    def test_get_artwork_id_found(self):
        self.add_test_data()
        result = artworkstore.get_artwork_by_id(self.aw1.id)
        self.assertEqual(result, self.aw1)

    def test_get_artwork_by_id_not_found(self):
        self.add_test_data()
        result = artworkstore.get_artwork_by_id(-1)
        self.assertIsNone(result)

    def test_delete_artwork_not_in_store_errors(self):
        self.add_test_data()
        at = Artwork(artwork_name='Not in store')
        with self.assertRaises(ArtworkError):
            artworkstore.delete_artwork(at)

    def test_count_artwork(self):
        self.add_test_data()
        count = artworkstore.artwork_count()
        self.assertEqual(3, count)

    def test_set_sold_artwork_sold(self):
        self.add_test_data()
        self.aw1.sold_artwork = True
        self.aw1.save()

        aw1_from_store = artworkstore.get_artwork_by_id(self.aw1.id)
        self.assertTrue(aw1_from_store.sold_artwork)

    def test_set_available_artwork(self):
        self.add_test_data()
        self.aw2.sold_artwork = True
        self.aw2.save()
        aw2_from_store = artworkstore.get_artwork_by_id(self.aw2.id)
        self.assertTrue(aw2_from_store.sold_artwork)

    def test_set_sold_artwork_available(self):
        self.add_test_data()

        self.aw1.sold_artwork = False
        self.aw1.save()

        aw1_from_store = artworkstore.get_artwork_by_id(self.aw1.id)
        self.assertFalse(aw1_from_store.sold_artwork)

    def test_set_available_artwork_available(self):
        self.add_test_data()
        self.aw2.sold_artwork = False
        self.aw2.save()

        aw2_from_store = artworkstore.get_artwork_by_id(self.aw2.id)
        self.assertFalse(aw2_from_store.sold_artwork)

    def test_is_artwork_in_store_present(self):
        self.add_test_data()
        self.assertTrue(artworkstore.exact_match(self.aw1))
        self.assertTrue(artworkstore.exact_match(self.aw2))
        self.assertTrue(artworkstore.exact_match(self.aw2))

    def test_is_artwork_in_store_not_present(self):
        not_in_store = Artwork(artwork_name='aaaa')
        self.add_test_data()
        self.assertFalse(artworkstore.exact_match(not_in_store))

    def test_is_artwork_in_store_empty_list(self):
        self.clear_artworkstore()
        not_in_store = Artwork(artwork_name='ccc')
        self.assertFalse(artworkstore.exact_match(not_in_store))

    def test_search_artwork_artist_match(self):
        self.add_test_data()
        self.assertCountEqual([self.aw1], artworkstore.search_artist('Picasso'))

    def test_search_artwork_name_match(self):
        self.add_test_data()
        self.assertCountEqual([self.aw1, self.aw2], artworkstore.search_artwork('Artwork'))

    def test_search_artwork_not_found(self):
        self.add_test_data()
        self.assertCountEqual([], artworkstore.search_artwork('Not in list'))

    def test_search_artwork_empty_store(self):
        self.clear_artworkstore()
        self.assertEqual([], artworkstore.search_artwork('No artwork here'))

    def test_search_artwork_case_insensitive_name_match(self):
        self.add_test_data()
        self.assertCountEqual([self.aw1, self.aw2], artworkstore.search_artwork('aRtWork'))

    def test_exact_match_not_found(self):
        self.add_test_data()
        aw = Artwork(artwork_name='Long sentences')
        self.assertTrue(artworkstore.exact_match(aw))

    def test_exact_match_not_found_name(self):
        self.add_test_data()
        aw = Artwork(artwork_name='Very long Sentence')
        self.assertFalse(artworkstore.exact_match(aw))

    def test_exact_match_not_found_empty_store(self):
        aw = Artwork(artwork_name='Whatever')
        self.clear_artworkstore()
        self.assertFalse(artworkstore.exact_match(aw))

    def test_get_artwork_sold_sold(self):
        self.add_test_data()
        sold_artwork = artworkstore.get_artwork_by_sold_value(True)
        self.assertCountEqual([self.aw2, self.aw3], sold_artwork)

    def test_get_artwork_sold_available(self):
        self.add_test_data()
        sold_artwork = artworkstore.get_artwork_by_sold_value(False)
        self.assertCountEqual([self.aw2, self.aw3], sold_artwork)
