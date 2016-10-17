#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="pystpr",
    packages=["pystpr", "pystpr.statistics", "pystpr.probabilities"],
    version="0.2",
    description="Easy to use Data Analysis functions for developers",
    author="João Ferreira",
    author_email="joao@joaodlf.com",
    url="https://github.com/joaodlf/pystpr",
    download_url="https://github.com/joaodlf/pystpr/tarball/0.2",
    keywords=["statistics", "probabilities"],
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scipy",

    ],
    classifiers=[],
)
