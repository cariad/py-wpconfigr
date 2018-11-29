""" Tests for the ConfigUpdater class. """

import unittest

from wp_configr import ConfigUpdater


class ConfigUpdaterTestCase(unittest.TestCase):
    """ Tests for the ConfigUpdater class. """

    def test_replace_bool(self):
        """ Asserts that boolean value is replaced. """

        config = 'define(\'WP_DEBUG\', false);'

        updater = ConfigUpdater(config=config)
        updater.update_property(key='WP_DEBUG', value=True)

        expected_config = 'define(\'WP_DEBUG\', true);'

        self.assertEqual(updater.config, expected_config)

    def test_replace_empty(self):
        """ Asserts that an empty value is replaced. """

        config = 'define(\'DB_USER\', \'\');'

        updater = ConfigUpdater(config=config)
        updater.update_property(key='DB_USER', value='updated-db-user')

        expected_config = 'define(\'DB_USER\', \'updated-db-user\');'

        self.assertEqual(updater.config, expected_config)

    def test_replace_value_with_spaces(self):
        """ Asserts that value containing spaces is replaced. """

        config = 'define(\'DB_USER\', \'foo bar\');'

        updater = ConfigUpdater(config=config)
        updater.update_property(key='DB_USER', value='updated-db-user')

        expected_config = 'define(\'DB_USER\', \'updated-db-user\');'

        self.assertEqual(updater.config, expected_config)

    def test_single_replacement(self):
        """ Asserts that a single match is replaced. """
        config = """
<?php
define('DB_NAME', 'foo');
define('DB_USER', 'bar');
"""

        updater = ConfigUpdater(config=config)
        updater.update_property(key='DB_NAME', value='updated-db-name')

        expected_config = """
<?php
define('DB_NAME', 'updated-db-name');
define('DB_USER', 'bar');
"""

        self.assertEqual(updater.config, expected_config)

    def test_space_variants(self):
        """ Asserts that spaces are handled. """

        def _assert(config, expect):
            updater = ConfigUpdater(config=config)
            updater.update_property(key='DB_NAME', value='new')
            self.assertEqual(updater.config, expect)

        _assert(config='define(\'DB_NAME\', \'old\');',
                expect='define(\'DB_NAME\', \'new\');')

        _assert(config=' define(\'DB_NAME\', \'old\');',
                expect=' define(\'DB_NAME\', \'new\');')

        _assert(config='define (\'DB_NAME\', \'old\');',
                expect='define (\'DB_NAME\', \'new\');')

        _assert(config='define( \'DB_NAME\', \'old\');',
                expect='define( \'DB_NAME\', \'new\');')

        _assert(config='define(\'DB_NAME\' , \'old\');',
                expect='define(\'DB_NAME\' , \'new\');')

        _assert(config='define(\'DB_NAME\',  \'old\');',
                expect='define(\'DB_NAME\',  \'new\');')

        _assert(config='define(\'DB_NAME\', \'old\' );',
                expect='define(\'DB_NAME\', \'new\' );')

        _assert(config='define(\'DB_NAME\', \'old\') ;',
                expect='define(\'DB_NAME\', \'new\') ;')

        _assert(config='define(\'DB_NAME\', \'old\'); ',
                expect='define(\'DB_NAME\', \'new\'); ')


if __name__ == '__main__':
    unittest.main()
