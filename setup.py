#!/usr/bin/env python

from setuptools import setup, find_packages

DISTNAME = 'solutions'
LICENSE = 'Modified BSD'
VERSION = '1.0'
SCRIPTS = ['bin/solutions']

if __name__ == '__main__':
    setup(
        name=DISTNAME,
        license=LICENSE,
        version=VERSION,
	scripts=SCRIPTS
    )
