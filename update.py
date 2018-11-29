"""
Update a wp-config.php file.
"""

import argparse

from wp_configr import FileUpdater


def run_from_cli():
    """
    Perform an update instigated from a CLI.
    """

    arg_parser = argparse.ArgumentParser(
        description='Update a wp-config.php file.')

    arg_parser.add_argument('--filename',
                            help='wp-config.php filename',
                            required=True)

    arg_parser.add_argument('--key',
                            help='Property key',
                            required=False)

    arg_parser.add_argument('--value',
                            help='New property value',
                            required=True)

    args = arg_parser.parse_args()

    updater = FileUpdater(filename=args.filename)
    updater.update_property(key=args.key, value=args.value)


if __name__ == '__main__':
    run_from_cli()
