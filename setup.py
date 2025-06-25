#!/usr/bin/env python3

import os
import re
from pathlib import Path

from setuptools import find_packages, setup

ROOT_DIR = os.path.dirname(__file__)
HERE = Path(__file__).parent

version = "0.12.0"

# Optional test requirements
try:
    with open("./test-requirements.txt") as test_reqs_txt:
        test_requirements = list(iter(test_reqs_txt))
except FileNotFoundError:
    test_requirements = []

try:
    long_description = open("README.rst").read()
except FileNotFoundError:
    long_description = ""

setup(
    name="aiosparql",
    version=version,
    description="An asynchronous SPARQL library using aiohttp",
    long_description=long_description,
    url="https://github.com/aio-libs/aiosparql",
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=["aiohttp>=3.5.0"],
    tests_require=test_requirements,
    zip_safe=False,
    test_suite="tests",
    python_requires=">=3.6.0",
    license="Apache 2",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
    maintainer="Cecile Tonglet",
    maintainer_email="cecile.tonglet@gmail.com",
)
