# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="ywh-collab",
    version="1.0",
    license="Apache",
    author="Aethios",
    author_email="tom.chambaretaud@protonmail.com",
    description="Yes We Hack private program comparator for hunters collaboration by Aethlios.",
    packages=find_packages(),
    install_requires=["requests"],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/AethliosIK/ywh-collab",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ]
)
