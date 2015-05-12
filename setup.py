# Release procedure
#
# Prepare the release:
#
#  - fill the changelog in README.rst
#  - run tests: tox
#  - update version in setup.py
#  - set release date in the changelog in README.rst
#  - check that "python setup.py sdist" contains all files tracked by
#    the SCM (Mercurial): update MANIFEST.in if needed
#  - git commit -a
#  - git tag VERSION
#  - git push --tags
#  - git push
#
# Release the new version:
#
#  - python setup.py register sdist bdist_wheel upload
#
# After the release:
#
#  - increment version in setup.py
#  - git commit && git push

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.rst") as fp:
    long_description = fp.read()

install_options = {
    "name": "sixer",
    "version": "0.1",
    "license": "Apache License 2.0",
    "author": 'Victor Stinner',
    "author_email": 'victor.stinner@gmail.com',

    "description": "Add Python 3 support to Python 2 applications using the six module.",
    "long_description": long_description,
    "url": "https://github.com/haypo/sixer",

    "classifiers": [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],

    "scripts": ["sixer.py"],
}

setup(**install_options)
