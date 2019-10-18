from unittest import TestCase
from unittest.mock import patch
import  database_config
database_config.database_path ='artworks.db'

import  artworkstore
from model import Artwork
from model import  Artist

import  ui
from Menu import Menu

class TestUI(TestCase):
    @patch('builtins.input', side_effect=['a'])
    @patch('builtins.print')
    def test_display_menu_get_choice(self, mock_print, mock_input):
        menu = Menu()
        menu.add_option('a', 'aaa', lambda: None)
        menu.add_option('b', 'bbb', lambda: None)

        self.assertEqual('a', ui.display_menu_get_choice(menu))

        mock_print.assert_any_call(menu)

    @patch('builtins.print')
    def test_message(self, mock_print):
        ui.message('hello')
        mock_print.assert_called_with('hello')

    @patch('builtins.print')
    def test_show_artwork_empty(self, mock_print):
        artworks = []
        ui.show_artworks(artworks)
        mock_print.assert_called_with('No books to display')

    @patch('builtins.print')
    def test_show_artwork_list(self,mock_print):
        aw1= Artwork('a','aaa')
        aw2= Artwork('b','bbb')
        artworks =[aw1,aw2]
        ui.show_artworks(artworks)

    @patch('builtins.input',side_effect=['artwork name'])
    def test_get_artwork_info(self,mock_input):
        artwork = ui.get_artwork_info()
        self.assertEqual('artwork name',artwork.artwork_name)

    @patch('builtins.print',side_effect=['31'])
    def test_get_artwork_id(self,mock_input):
        self.assertEqual(31,ui.get_artwork_id())

    @patch('builtins.input', side_effect=['no', '-4', '0', 'cbaba', 'cheese cheese cheese', '33 33 33 ', '3'])
    def test_get_artwork_id_rejects_non_positive_integer(self, mock_input):
        self.assertEqual(3, ui.get_artwork_id())

    @patch('builtins.input', side_effect=['available'])
    def test_get_artwork_value_available(self, mock_input):
        self.assertTrue(ui.get_sold_value())

    @patch('builtins.input', side_effect=['sold'])
    def test_get_sold_value_available(self, mock_input):
        self.assertFalse(ui.get_sold_value())

    @patch('builtins.input', side_effect=['not one of the options', 'pizza', '1234', 'Not', 'rea', 'sold'])
    def test_get_sold_value_validates(self, mock_input):
        self.assertTrue(ui.get_sold_value())

    @patch('builtins.input', side_effect=['cheese'])
    @patch('builtins.print')
    def ask_question(self, mock_print, mock_input):
        self.assertEqual('cheese', ui.ask_question('What is the best portrait?'))
        mock_print.assert_called_with('What is the best portrait')


