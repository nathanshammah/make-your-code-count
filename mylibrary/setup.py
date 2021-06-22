#!/usr/bin/env python
"""
Setup file created
"""
from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='mylibrary',
      version='0.1',
      description='Test',
      author='Shahnawaz Ahmed, Nathan Shammah',
      packages=['mylibrary'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Framework:: Jupyter",
          "Intended Audience :: Science/Research",
          "Natural Language :: English",
          "Topic:: Education"
          "Topic:: Documentation :: Sphinx",
          "Topic:: Software Development:: Build Tools",
          "Topic:: Software Development:: Libraries:: nbconvert",
          "Topic :: Software Development :: Testing",
          "Topic :: Software Development :: Version Control :: Git",
      ],
      )
