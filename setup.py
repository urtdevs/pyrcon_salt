#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

import os
import setuptools

base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(base_dir, "pyrcon_salt", "__about__.py")) as f:
    exec(f.read(), about)

with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()

setuptools.setup(
    name=about["__title__"],
    version=about["__version__"],

    description=about["__summary__"],
    long_description=long_description,
    license=about["__license__"],
    url=about["__uri__"],

    author=about["__author__"],
    author_email=about["__email__"],

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: System :: Systems Administration"
    ],

    packages=["pyrcon_salt"],
    install_requires=[
        "pyrcon == 0.0.1"
    ],
    test_suite='nose.collector'
)
