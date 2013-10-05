#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
## To deploy use
## $ python ./setup.py sdist upload
##
## Your need increase version before it !!!
##

from __future__ import unicode_literals

from distutils.core import setup

#packages = find_packages()
ConsoleScripts = [
    'quantum-fdb-cleaner = fdb_cleaner.cli:main',
]

setup(
    name='fdb_cleaner',
    version='0.0.1',
    packages=['fdb_cleaner'],
    url='https://github.com/xenolog/fdb_cleaner',
    license='Apache License, version 2.0',
    author='Sergey Vasilenko',
    author_email='svasilenko@mirantis.com',
    description='tool for clean ovs FDB table ',
    #setup_requires=[
    #    'distribute>=0.6',
    #],
    include_package_data=True,
    long_description=open('README.md').read(),
    platforms='All',
    classifiers=[
        'Environment :: Other Environment',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Natural Language :: Russian',
        'Development Status :: 4 - Beta',
        #'Topic :: Software Development :: Libraries',
    ],
    entry_points={'console_scripts': ConsoleScripts},
    zip_safe=False
)
# vim: tabstop=4 shiftwidth=4 softtabstop=4