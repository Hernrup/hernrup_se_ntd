#!/usr/bin/env python
# from distutils.core import setup
from setuptools import setup, command
from os import path


def readme():
    with open(path.join(path.abspath(path.dirname(__file__)),
                        'README.rst')) as f:
        return f.read()


setup(
    name='hernrup-ntd',
    version='0.0.1',

    packages=[],

    install_requires=[
        'hernrup-portal'
    ],

    setup_requires=[
        'flake8==2.1.0',
        'describe-it==1.1.0',
        'nose==1.3.3',
        'PyHamcrest==1.8.1',
        'wheel==0.22.0',
    ],

    dependency_links=[

    ],

    entry_points={
        'console_scripts': [
            'blog = hernrup_se.common.manage:main'
        ],

    }

)
