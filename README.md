# wpconfigger

[![CircleCI](https://circleci.com/gh/cariad/py-wpconfigr/tree/master.svg?style=svg)](https://circleci.com/gh/cariad/py-wpconfigr/tree/master)

A Python package for reading and writing configuration values in a WordPress `wp-config.php` file.

## Overview

A default `wp-config.php` might look like this:

```php
<?php
define( 'DB_NAME', 'database_name_here' );
```

`wpconfigger` will help you update the file to:

```php
<?php
define( 'SOMETHING_ENTIRELY_NEW', 'garnet' );
define( 'DB_NAME', 'my_blog' );
```

`wpconfigger` exposes two functions:

- `set(key, value)` will update a property of name `key` if it exists, otherwise will create it.
- `get(key)` will return the value of the property of name `key`, or `None` if it doesn't exist.


## Installation

```shell
pip install wpconfigger
```

## Command-line usage

### Writing values to wp-config.php

Named parameters:

- `--filename`: Full path and filename of the `wp-config.php` file.
- `--key`: Name of the property to create/update.
- `--value`: String value to set.
- `--set-true`: Set the value to boolean `true`.
- `--set-false`: Set the value to boolean `false`.
- `--log-level`: (Optional) Log level.

```shell
python -m wpconfigger --filename  /www/wp-config.php \
                      --key       DB_NAME \
                      --value     my_blog \
                      --log-level info
```

### Reading values from wp-config.php

As above, but do not specify a value (via the `--value`, `--set-true` or `--set-false` arguments).

```shell
python -m wpconfigger --filename /www/wp-config.php \
                      --key      DB_NAME
```

### Code usage

To update a string holding `wp-config.php` content:

```python
from wpconfigr import WpConfigString

config = WpConfigString(config_string)
config.set('DB_NAME', 'my_blog')
updated_config_string = config.content
```

To directly update a `wp-config.php` file:

```python
from wpconfigger import WpConfigFile

config = WpConfigFile(filename)
config.set('DB_NAME', 'my_blog')
# File is updated immediately after each property update.
```

To read a property value:

```python
db_name = config.get('DB_NAME')
```

## Development

### Prerequisites

`wpconfigger` requires Python 3.x.

### Installing dependencies

```shell
pip install -e .[dev]
```

### Running tests

```shell
python test.py
```

## Changelog

### v1.0.0 - 2022-07-09

- Renamed and republished as `wpconfigger`.

### v1.4 - 2018-12-06

- Fixed bug where commented properties were read and updated.

### v1.3 - 2018-12-02

- Added `--set-true` and `--set-false` command-line flags.

### v1.2 - 2018-12-02

- No longer re-writes the configuration file if nothing has changed.

### v1.1 - 2018-12-02

- Added logging.
  - Test runs log everything.
  - Running from the command-line logs only `CRITICAL` by default, but can be overridden with the new optional `--log-level` argument.
- Made the documentation a little clearer, and fixed a typo in a code sample.
- Replaced internal naming references to `FRACTIONAL` with `FLOAT`. The word utterly eluded me for v1.0.
- Fixed some code formatting and Pylint warnings.
- Ignore `coverage` HTML reports in source control.

### v1.0 - 2018-12-01

- Initial release.
