
"""
Read and write properties in a 'wp-config.php' file.
"""

from wp_configr import WpConfigString

class WpConfigFile(WpConfigString):
    """
    Read and write properties in a 'wp-config.php' file.

    Args:
        filename (str): Filename of the 'wp-config.php' file.
    """

    def __init__(self, filename):
        self._filename = filename

        with open(self._filename, 'r') as stream:
            content = stream.read()

        super().__init__(content=content)

    def update(self, key, value):
        """
        Updates the value of the given key in the file.

        Args:
            key (str): Key of the property to update.
            value (str): New value of the property.
        """

        super().update(key=key, value=value)

        with open(self._filename, 'w') as stream:
            stream.write(self.content)
