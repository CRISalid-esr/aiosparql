#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="aiosparql",  # ✅ hardcoded
    version="0.12.0",  # ✅ hardcoded
    description="An asynchronous SPARQL library using aiohttp",
    url="https://github.com/aio-libs/aiosparql",
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=["aiohttp>=3.5.0"],
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
