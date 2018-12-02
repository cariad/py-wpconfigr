"""
Update a wp-config.php file.
"""

import argparse

from logging import basicConfig

from wpconfigr import WpConfigFile


def run_from_cli():
    """
    Perform an update instigated from a CLI.
    """

    arg_parser = argparse.ArgumentParser(
        description='Read and write properties in a wp-config.php file. '
                    'Include a --value argument to set the value, omit it to '
                    'read the value of the specified key.',
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

    arg_parser.add_argument('--log-level',
                            default='CRITICAL',
                            help='Log level',
                            required=False)

    arg_parser.add_argument('--set-true',
                            action='store_true',
                            help='Set the value as boolean true')

    arg_parser.add_argument('--set-false',
                            action='store_true',
                            help='Set the value as boolean false')

    args = arg_parser.parse_args()

    if args.set_true and args.set_false:
        arg_parser.error('Cannot set --set-true and --set-false.')

    if args.value and args.set_true:
        arg_parser.error('Cannot set --value and --set-true.')

    if args.value and args.set_false:
        arg_parser.error('Cannot set --value and --set-false.')

    basicConfig(level=str(args.log_level).upper())

    updater = WpConfigFile(filename=args.filename)

    if args.set_true:
        value = True
    elif args.set_false:
        value = False
    else:
        value = args.value

    if value is not None:
        updater.set(key=args.key, value=value)
    else:
        got = updater.get(key=args.key)

        if got:
            print(got)


if __name__ == '__main__':
    run_from_cli()
