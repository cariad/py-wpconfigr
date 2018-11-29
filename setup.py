"""
"wp-configr" package setup.
"""

from setuptools import setup

setup(
    name='wp-configr',
    version='0.2',
    description='Applies updates to WordPress wp-config.php files.',
    url='https://github.com/cariad/wp-configr',
    author='Cariad Eccleston',
    author_email='cariad@cariad.me',
    license='MIT',
    packages=[
        'wp_configr'
    ],
    install_requires=[
    ],
    extras_require={
        'dev': [
            'coverage',
            'pylint'
        ]
    }
)
