"""
Configurations of the Distribution.
"""

from distutils.core import setup

setup(
    name = 'pyxample',
    version = '0.1.1',
    license = 'BSD',
    description = 'An project in Python.',
    long_description = __doc__,
    author = 'Jose Leonel L. Buzzo',
    author_email = 'lbuzzo@mochsl.org.br',
    url = None,
    classifiers = [],
    packages = [ 'pyxample' ],
    package_dir = {'': 'lib'},
    py_modules = [ 'UI' ],
    scripts = [ 'pyxpl' ]
    )
