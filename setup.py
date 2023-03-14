#!/usr/bin/env python
import logging
import os
from importlib import util
from os import path

import setuptools
from setuptools import setup

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

logger = logging.getLogger(__name__)
spec = util.spec_from_file_location(
    "bridgecrew.version", os.path.join("bridgecrew", "version.py")
)
# noinspection PyUnresolvedReferences
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)  # type: ignore
version = mod.version  # type: ignore

setup(
    install_requires=[
        f"checkov=={version}",
    ],
    license="Apache License 2.0",
    name="bridgecrew",
    version=version,
    description="Infrastructure as code static analysis",
    author="bridgecrew",
    author_email="meet@bridgecrew.io",
    url="https://github.com/bridgecrewio/bridgecrew",
    packages=setuptools.find_packages(exclude=["tests*"]),
    scripts=["bin/bridgecrew", "bin/bridgecrew.cmd"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        'Topic :: Security',
        'Topic :: Software Development :: Build Tools'
    ]
)
