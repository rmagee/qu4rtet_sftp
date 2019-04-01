#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['paramiko']

setup_requirements = ['paramiko', 'python-dotenv']

test_requirements = ['paramiko' ]

setup(
    author="SerialLab, Corp.",
    author_email='slab@serial-lab.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="QU4RTET SFTP Tools and Utilities",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='quartet_sftp',
    name='quartet_sftp',
    packages=find_packages(include=['quartet_sftp']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://gitlab.com/serial-lab/quartet_sftp',
    version='0.1.0',
    zip_safe=False,
)
