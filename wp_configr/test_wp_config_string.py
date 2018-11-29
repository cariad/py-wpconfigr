""" Tests for the WpConfigString class. """

import unittest

from wp_configr.wp_config_string import WpConfigString


class GetTestCase(unittest.TestCase):
    """ Tests for the get function. """

    def test_string_property_exists(self):
        """ Asserts that the string property is found. """

        config = """
<?php
define('DB_NAME', 'foo');
define('DB_USER', 'bar');
"""

        config = WpConfigString(content=config)
        self.assertEqual(config.get(key='DB_USER'), 'bar')

    def test_bool_property_exists(self):
        """ Asserts that the boolean property is found. """

        config = """
<?php
define('WP_DEBUG', true);
"""

        config = WpConfigString(content=config)
        self.assertTrue(config.get(key='WP_DEBUG'))

    def test_property_not_exists(self):
        """ Asserts that None is returned. """

        config = """
<?php
define('DB_NAME', 'foo');
define('DB_USER', 'bar');
"""

        config = WpConfigString(content=config)
        self.assertIsNone(config.get(key='NOPE'))

class UpdateTestCase(unittest.TestCase):
    """ Tests for the update method. """

    def test_replace_bool(self):
        """ Asserts that boolean value is replaced. """

        config = WpConfigString(content='define(\'WP_DEBUG\', false);')
        config.update(key='WP_DEBUG', value=True)
        self.assertEqual(config.content, 'define(\'WP_DEBUG\', true);')

    def test_replace_empty(self):
        """ Asserts that an empty value is replaced. """

        config = 'define(\'DB_USER\', \'\');'

        updater = WpConfigString(content=config)
        updater.update(key='DB_USER', value='updated-db-user')

        expected_config = 'define(\'DB_USER\', \'updated-db-user\');'

        self.assertEqual(updater.content, expected_config)

    def test_replace_value_with_spaces(self):
        """ Asserts that value containing spaces is replaced. """

        config = 'define(\'DB_USER\', \'foo bar\');'

        updater = WpConfigString(content=config)
        updater.update(key='DB_USER', value='updated-db-user')

        expected_config = 'define(\'DB_USER\', \'updated-db-user\');'

        self.assertEqual(updater.content, expected_config)

    def test_single_replacement(self):
        """ Asserts that a single match is replaced. """
        config = """
<?php
define('DB_NAME', 'foo');
define('DB_USER', 'bar');
"""

        updater = WpConfigString(content=config)
        updater.update(key='DB_NAME', value='updated-db-name')

        expected_config = """
<?php
define('DB_NAME', 'updated-db-name');
define('DB_USER', 'bar');
"""

        self.assertEqual(updater.content, expected_config)

    def test_space_variants(self):
        """ Asserts that spaces are handled. """

        def _assert(config, expect):
            updater = WpConfigString(content=config)
            updater.update(key='DB_NAME', value='new')
            self.assertEqual(updater.content, expect)

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
