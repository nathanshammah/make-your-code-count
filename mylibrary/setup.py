#!/usr/bin/env python
"""
Setup file
"""
from setuptools import setup, find_packages

setup(name='mylibrary',
      version='0.0.1',
      description='Test library',
      author='Shahnawaz Ahmed, Nathan Shammah',
      packages = find_packages(include=['mylibrary', 'mylibrary.*'])
     )
