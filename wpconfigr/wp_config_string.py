"""
Read and write properties in a string in the format of a 'wp-config.php' file.
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
    def get_value_from_match(match):
        """
        Gets the value of the property in the given MatchObject.

        Args:
            match (MatchObject): The matched property.

        Return:
            The discovered value, as a string or boolean.
        """

        value = match.groups(1)[0]
        clean_value = str(value).lstrip().rstrip()

        if clean_value == 'true':
            return True

        if clean_value == 'false':
            return False

        try:
            return float(clean_value)
        except ValueError:
            return clean_value

    @property
    def content(self):
        """ Gets the loaded content. """

        return self._content

    def _get_string_match(self, key):
        """
        Gets a MatchObject for the given key, assuming a string value.

        Args:
            key (str): Key of the property to look-up.

        Return:
            MatchObject: The discovered match.
        """

        expression = r'(?:\s*)'.join([
            'define',
            r'\(',
            '\'{}\''.format(key),
            ',',
            r'\'(.*)\'',
            r'\)',
            ';'
        ])

        pattern = re.compile(expression, re.MULTILINE)
        return pattern.search(self._content)

    def _get_non_string_match(self, key):
        """
        Gets a MatchObject for the given key, assuming a non-string value.

        Args:
            key (str): Key of the property to look-up.

        Return:
            MatchObject: The discovered match.
        """

        expression = r'(?:\s*)'.join([
            'define',
            r'\(',
            '\'{}\''.format(key),
            ',',
            r'(.*)',
            r'\)',
            ';'
        ])

        pattern = re.compile(expression, re.MULTILINE)
        return pattern.search(self._content)

    def _get_match(self, key):
        """
        Gets a MatchObject for the given key.

        Args:
            key (str): Key of the property to look-up.

        Return:
            MatchObject: The discovered match.
        """

        return self._get_string_match(key=key) or \
            self._get_non_string_match(key=key)

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

    def set(self, key, value):
        """
        Updates the value of the given key in the loaded content.

        Args:
            key (str): Key of the property to update.
            value (str): New value of the property.
        """

        match = self._get_match(key=key)

        if not match:
            if isinstance(value, str):
                value_str = '\'{}\''.format(value)
            else:
                value_str = str(value).lower()

            new = 'define(\'{key}\', {value});\n'.format(
                key=key,
                value=value_str)

            self._content = self._content.replace('<?php\n', '<?php\n' + new)
            return

        if WpConfigString.get_value_from_match(match=match) == value:
            return

        start_index = match.start(1)
        end_index = match.end(1)

        if isinstance(value, bool):
            value = str(value).lower()

        start = self._content[:start_index]
        end = self._content[end_index:]

        self._content = start + value + end
