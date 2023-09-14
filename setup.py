#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module sets up the package for the bennie_bash"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bennie_bash",
    author="O Hung Lun",
    author_email="hunglun.o@gmail.com",
    maintainer="O Hung Lun",
    maintainer_email="hunglun.o@gmail.com",
    version="0.1.0",
    url="https://github.com/hunglun/bennie_bash",
    download_url="https://github.com/hunglun/bennie_bash",
    keywords=["bash", "BennieBash"],
    license="GNU",
    description="Personal Bash Shell",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/hunglun/bennie_bash/issues",
    },
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pytest",
    ],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "bennie_bash = bennie_bash.__main__:main",
        ]
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
