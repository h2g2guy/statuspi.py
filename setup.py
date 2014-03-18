#!/bin/env python
# -*- coding: utf8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="statuspi.py",
    version=version,
    description="A simple headless status box utility for the Raspberry Pi.",
    long_description=open('README.rst').read(),
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    ],
    keywords="",
    author="Joe Trotta",
    author_email="jht6437@rit.edu",
    url="http://github.com/h2g2guy/statuspi.py",
    license="GPLv3+",
    packages=find_packages(
    ),
    scripts=[
        "distribute_setup.py",
        "bin/statuspi.py",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "RPi.GPIO",
    ],
    #TODO: Deal with entry_points
    #entry_points="""
    #[console_scripts]
    #pythong = pythong.util:parse_args
    #"""
)
