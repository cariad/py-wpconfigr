"""
"wpconfigr" package setup.
"""

from setuptools import setup

with open('README.md', 'r') as stream:
    LONG_DESCRIPTION = stream.read()

setup(
    author='Cariad Eccleston',
    author_email='cariad@cariad.me',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Site Management'
    ],
    description='Read and write configuration values in a WordPress '
                '"wp-config.php" file.',
    extras_require={
        'dev': [
            'autopep8',
            'coverage',
            'pylint'
        ]
    },
    name='wpconfigr',
    license='MIT',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=[
        'wpconfigr'
    ],
    url='https://github.com/cariad/py-wpconfigr',
    version='1.3'
)
