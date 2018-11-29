"""
Updates properties in a string in the format of a 'wp-config.php' file.
"""

import re


class ConfigUpdater():
    """
    Updates properties in a string in the format of a 'wp-config.php' file.

    Args:
        config (str): The string content of a 'wp-config.php' file
    """

    def __init__(self, config):
        self._config = config

    @staticmethod
    def get_expression_for_property(key):
        """
        Gets a regular expression to match a property with the given key.

        Args:
            key (str): Key of the property to look-up.

        Returns:
            str: Regular expression.
        """

        return r'(?:\s*)'.join([
            'define',
            r'\(',
            '\'{}\''.format(key),
            ',',
            r'((?:\')?[^\']*)(?:\')?',
            r'\)',
            ';'
        ])

    @staticmethod
    def get_pattern_for_property(key):
        """
        Gets a compiled regular expression pattern to match a property with the
        given key.

        Args:
            key (str): Key of the property to look-up.

        Returns:
            Pattern: Compiled regular expression pattern.
        """

        return re.compile(ConfigUpdater.get_expression_for_property(key),
                          re.MULTILINE)

    @property
    def config(self):
        """ Gets the loaded content. """

        return self._config

    def update_property(self, key, value):
        """
        Updates the value of the given key in the loaded content.

        Args:
            key (str): Key of the property to update.
            value (str): New value of the property.
        """

        pattern = ConfigUpdater.get_pattern_for_property(key)
        match = pattern.search(self._config)

        if not match:
            return

        if match.groups(1) == value:
            return

        start_index = match.start(1)
        end_index = match.end(1)

        if isinstance(value, str):
            start_index = start_index + 1

        if isinstance(value, bool):
            value = str(value).lower()

        start = self._config[:start_index]
        end = self._config[end_index:]

        self._config = start + value + end
