# wp-configr

A Python package for updating the property values in a WordPress `wp-config.php` file.

## CI status

[![CircleCI](https://circleci.com/gh/cariad/wp-configr/tree/master.svg?style=svg)](https://circleci.com/gh/cariad/wp-configr/tree/master)

## Example

A default `wp-config.php` might look like this:

```php
<?php
/** The name of the database for WordPress */
define( 'DB_NAME', 'database_name_here' );
/** MySQL database username */
define( 'DB_USER', 'username_here' );
```

This package will allow you to update the file to:

```php
<?php
/** The name of the database for WordPress */
define( 'DB_NAME', 'myblog' );
/** MySQL database username */
define( 'DB_USER', 'wp_user' );
```

## Usage

### I just want to update a `wp-config.php` file!

```shell
python update.py --filename <filename> --key <key> --value <value>
```

For example:

```shell
python update.py --filename /mnt/www/wp-config.php --key DB_NAME --value myblog
```

### Installation as project dependency

```shell
pip install git+git://github.com/cariad/wp-configr
```

### Code sample

To update in-memory `wp-config.php` string content:

```python
from wp_configr import ConfigUpdater

updater = ConfigUpdater(config=your_config_string)

updater.update_property('DB_NAME', 'myblog')
updater.update_property('DB_USER', 'wp_user')
updater.update_property('WP_DEBUG', True)

updated_config_string = updater.config
```

To update a `wp-config.php` file:

```python
from wp_configr import FileUpdater

updater = FileUpdater(filename=your_filename)

updater.update_property('DB_NAME', 'myblog')
updater.update_property('DB_USER', 'wp_user')
updater.update_property('WP_DEBUG', True)

# File is updated immediately after each property update.
```

## Development

### Prerequisites

wp-configr requires Python 3.x.

### Installing development dependencies

```shell
pip install -e .[dev]
```

### Running tests

```shell
python test.py
```
