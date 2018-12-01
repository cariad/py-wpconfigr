""" Tests for the WpConfigString class. """

import unittest

from wpconfigr import WpConfigString


class GetTestCase(unittest.TestCase):
    """ Tests for the get function. """

    @classmethod
    def setUpClass(cls):
        cls.config = WpConfigString(content="""
<?php
define('STRING',     'foo');
define('TRUE',       true);
define('FALSE',      false);
define('INTEGER',    1);
define('FRACTIONAL', 2.3);
""")

    def test_string(self):
        """ Asserts that a string value is returned. """
        self.assertEqual(self.config.get(key='STRING'), 'foo')

    def test_true_bool(self):
        """ Asserts that a true boolean value is returned. """
        self.assertTrue(self.config.get(key='TRUE'))

    def test_false_bool(self):
        """ Asserts that a false boolean value is returned. """
        self.assertFalse(self.config.get(key='FALSE'))

    def test_integer(self):
        """ Asserts that an integer value is returned. """
        self.assertEqual(self.config.get(key='INTEGER'), 1)

    def test_fractional(self):
        """ Asserts that a fractional number value is returned. """
        self.assertEqual(self.config.get(key='FRACTIONAL'), 2.3)

    def test_property_not_exists(self):
        """ Asserts that missing values are returned as None. """
        self.assertIsNone(self.config.get(key='NOPE'))


if __name__ == '__main__':
    unittest.main()
