""" Tests for the WpConfigString class. """

import unittest

from logging import basicConfig

from wpconfigr import WpConfigString

basicConfig(level='DEBUG')


class GetTestCase(unittest.TestCase):
    """ Tests for the get function. """

    @classmethod
    def setUpClass(cls):
        cls.config = WpConfigString(content="""
<?php
define('STRING',  'foo');
define('TRUE',    true);
define('FALSE',   false);
define('INTEGER', 1);
define('FLOAT',   2.3);
// define('COMMENTED_STRING', 'jam);
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

    def test_float(self):
        """ Asserts that a float value is returned. """
        self.assertEqual(self.config.get(key='FLOAT'), 2.3)

    def test_comments(self):
        """ Asserts that a commented value is not returned. """
        self.assertIsNone(self.config.get(key='COMMENTED_STRING'))

    def test_property_not_exists(self):
        """ Asserts that missing values are returned as None. """
        self.assertIsNone(self.config.get(key='NOPE'))


if __name__ == '__main__':
    unittest.main()
