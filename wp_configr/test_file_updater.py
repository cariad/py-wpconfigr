""" Tests for the ConfigUpdater class. """

import os
import shutil
import unittest

from wp_configr import FileUpdater


class FileTestCase(unittest.TestCase):
    """ Tests for the ConfigUpdater class. """

    def test(self):
        """ Asserts that the file is updated as-expected. """

        this_dir = os.path.dirname(os.path.realpath(__file__))

        original_file = os.path.join(this_dir, 'wp-config-sample.original.php')
        actual_file = os.path.join(this_dir, 'wp-config-sample.actual.php')
        expected_file = os.path.join(this_dir, 'wp-config-sample.expected.php')

        if os.path.exists(actual_file):
            os.unlink(actual_file)

        shutil.copy(original_file, actual_file)

        updater = FileUpdater(actual_file)

        updater.update_property('DB_NAME', 'updated-db-name')
        updater.update_property('DB_USER', 'updated-db-user')
        updater.update_property('DB_COLLATE', 'updated-db-collate')
        updater.update_property('AUTH_KEY', 'updated-auth-key')
        updater.update_property('WP_DEBUG', True)

        with open(actual_file, 'r') as stream:
            actual = stream.readlines()

        os.unlink(actual_file)

        with open(expected_file, 'r') as stream:
            expected = stream.readlines()

        self.maxDiff = None  # pylint: disable=invalid-name
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
