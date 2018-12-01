# wp-configr

[![CircleCI](https://circleci.com/gh/cariad/py-wpconfigr/tree/master.svg?style=svg)](https://circleci.com/gh/cariad/py-wpconfigr/tree/master)

A Python package for reading and writing configuration values in a WordPress `wp-config.php` file.

## Example

A default `wp-config.php` might look like this:

```php
<?php
define( 'DB_NAME', 'database_name_here' );
```

This package will allow you to update the file to:

```php
<?php
define( 'SOMETHING_ENTIRELY_NEW', 'garnet' );
define( 'DB_NAME', 'my_blog' );
```

## Installation

```shell
pip install wpconfigr
```

## Command-line usage

To set a value:

```shell
python -m wpconfigr --filename <filename> --key <key> --value <value>
```

To read a value:

```shell
python -m wpconfigr --filename <filename> --key <key>
```

For example:

```shell
python -m wpconfigr --filename /mnt/www/wp-config.php --key DB_NAME
> database_name_here

python -m wpconfigr --filename /mnt/www/wp-config.php --key DB_NAME --value my_blog
python -m wpconfigr --filename /mnt/www/wp-config.php --key DB_NAME
> my_blog

python -m wpconfigr --filename /mnt/www/wp-config.php --key SOMETHING_ENTIRELY_NEW
# No value returned.

python -m wpconfigr --filename /mnt/www/wp-config.php --key SOMETHING_ENTIRELY_NEW --value garnet
python -m wpconfigr --filename /mnt/www/wp-config.php --key SOMETHING_ENTIRELY_NEW
> garnet
```

### Code usage

To update a string holding `wp-config.php` content:

```python
from wpconfigr import WpConfigString

config = WpConfigString(content=your_config_string)
config.set('DB_NAME', 'my_blog')
updated_config_string = updater.content
```

To directly update a `wp-config.php` file:

```python
from wpconfigr import WpConfigFile

config = WpConfigFile(filename=your_filename)
config.set('DB_NAME', 'my_blog')
# File is updated immediately after each property update.
```

To read a property value:

```python
db_name = config.get('DB_NAME')
```

## Development

### Prerequisites

wp-configr requires Python 3.x.

### Installing dependencies

```shell
pip install -e .[dev]
```

### Running tests

```shell
python test.py
```
