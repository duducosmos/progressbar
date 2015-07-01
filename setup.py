#!/usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = "Simple Progress Bar"
__author__ = "Eduardo S. Pereira"
__email__ = "pereira.somoza@gmail.com"
__data__ = "01/07/2015"
__versio__ = "0.1"

import os


from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="progressbar",
    version="0.1.0",
    author="Eduardo dos Santos Pereira",
    author_email="pereira.somoza@gmail.com",
    description=("Simple progress bar"),
    license = "GNU v3",
    packages= find_packages(),
    keywords = "progress bar",
    url = "https://github.com/duducosmos/progressbar",
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: GNU V3",
    ],
)