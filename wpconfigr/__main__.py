"""
Update a wp-config.php file.
"""

import argparse

from wpconfigr import WpConfigFile


def run_from_cli():
    """
    Perform an update instigated from a CLI.
    """

    arg_parser = argparse.ArgumentParser(
        description='Read and write properties in a wp-config.php file. Include a --value argument to set the value, omit it to read the value of the specified key.',
        prog='python -m wpconfigr')

    arg_parser.add_argument('--filename',
                            help='wp-config.php filename',
                            required=True)

    arg_parser.add_argument('--key',
                            help='Property key',
                            required=True)

    arg_parser.add_argument('--value',
                            help='New property value',
                            required=False)

    args = arg_parser.parse_args()

    updater = WpConfigFile(filename=args.filename)

    if args.value:
        updater.set(key=args.key, value=args.value)
    else:
        got = updater.get(key=args.key)

        if got:
            print(got)


if __name__ == '__main__':
    run_from_cli()
