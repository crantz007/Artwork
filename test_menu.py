from unittest import TestCase
from Menu import Menu


class TestMenu(TestCase):
    def setUp(self):
        self.Menu = Menu()

        def a():
            pass

        def b():
            pass

        self.a = a
        self.b = b

        self.Menu.add_option('a', 'aaaa', a)
        self.Menu.add_option('b', 'bbbb', b)

    def test_add_option(self):
        self.assertDictEqual({'a': 'aaaaa', 'b': 'bbbb'}, self.Menu.text_descript)
        self.assertDictEqual({'a': self.a, 'b': self.b}, self.Menu.functions)

    def test_is_valid(self):
        self.assertTrue(self.Menu.is_valid('a'))
        self.assertTrue(self.Menu.is_valid('b'))

    def test_is_not_valid(self):
        self.assertFalse(self.Menu.is_valid('aa'))
        self.assertFalse(self.Menu.is_valid('c'))

    def test_get_action(self):
        self.assertEqual(self.a, self.Menu.get_action('a'))
        self.assertEqual(self.b, self.Menu.get_action('b'))

    def test_get_action_returns_none_if_in_menu(self):
        self.assertIsNone(self.Menu.get_action('aa'))
        self.assertIsNone(self.Menu.get_action('c'))

    def test_string(self):
        menu_string = 'a: aaaa\nb: bbbb'
        self.assertEqual(menu_string, str(self.Menu))
