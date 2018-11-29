"""
Read and write  properties in a string in the format of a 'wp-config.php' file.
"""

import re


class WpConfigString():
    """
    Read and write properties in a string in the format of a 'wp-config.php'
    file.

    Args:
        content (str): The string content of a 'wp-config.php' file
    """

    def __init__(self, content):
        self._content = content

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

        return re.compile(WpConfigString.get_expression_for_property(key),
                          re.MULTILINE)

    @staticmethod
    def get_value_from_match(match):
        """
        Gets the value of the property in the given MatchObject.

        Args:
            match (MatchObject): The matched property.

        Return:
            str: The discovered value.
        """

        value = match.groups(1)[0]

        if isinstance(value, str):
            return value[1:]

        return value

    @property
    def content(self):
        """ Gets the loaded content. """

        return self._content

    def _get_match(self, key):
        """
        Gets a MatchObject for the given key.

        Args:
            key (str): Key of the property to look-up.

        Return:
            MatchObject: The discovered match.
        """

        pattern = WpConfigString.get_pattern_for_property(key)
        return pattern.search(self._content)

    def get(self, key):
        """
        Gets the value of the property of the given key.

        Args:
            key (str): Key of the property to look-up.
        """

        match = self._get_match(key=key)

        if not match:
            return None

        return WpConfigString.get_value_from_match(match=match)

    def update(self, key, value):
        """
        Updates the value of the given key in the loaded content.

        Args:
            key (str): Key of the property to update.
            value (str): New value of the property.
        """

        match = self._get_match(key=key)

        if not match:
            return

        if WpConfigString.get_value_from_match(match=match) == value:
            return

        start_index = match.start(1)
        end_index = match.end(1)

        if isinstance(value, str):
            start_index = start_index + 1

        if isinstance(value, bool):
            value = str(value).lower()

        start = self._content[:start_index]
        end = self._content[end_index:]

        self._content = start + value + end
