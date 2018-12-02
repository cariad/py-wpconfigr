""" Tests for the ConfigUpdater class. """

import os
import shutil
import unittest

from logging import basicConfig

from wpconfigr import WpConfigFile

basicConfig(level='DEBUG')


class FileTestCase(unittest.TestCase):
    """ Tests for the ConfigUpdater class. """

    @classmethod
    def setUpClass(cls):
        cls.this_dir = os.path.dirname(os.path.realpath(__file__))
        cls.original_file = os.path.join(
            cls.this_dir, 'wp-config-sample.original.php')

    def test_read(self):
        """ Asserts that a value can be read from a file. """

        config = WpConfigFile(filename=self.original_file)
        self.assertEqual(config.get('DB_PASSWORD'), 'password_here')

    def test_write(self):
        """ Asserts that the file is updated as-expected. """

        actual_file = os.path.join(self.this_dir,
                                   'wp-config-sample.actual.php')

        expected_file = os.path.join(self.this_dir,
                                     'wp-config-sample.expected.php')

        if os.path.exists(actual_file):
            os.unlink(actual_file)

        shutil.copy(self.original_file, actual_file)

        config = WpConfigFile(filename=actual_file)

        config.set('DB_NAME', 'updated-db-name')
        config.set('DB_USER', 'updated-db-user')
        config.set('DB_COLLATE', 'updated-db-collate')
        config.set('AUTH_KEY', 'updated-auth-key')
        config.set('WP_DEBUG', True)
        config.set('WP_NEW_STRING', 'bar')
        config.set('WP_NEW_TRUE', True)
        config.set('WP_NEW_FALSE', False)

        with open(actual_file, 'r') as stream:
            actual = stream.readlines()

        os.unlink(actual_file)

        with open(expected_file, 'r') as stream:
            expected = stream.readlines()

        self.maxDiff = None  # pylint: disable=invalid-name
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
