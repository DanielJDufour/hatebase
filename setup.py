from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding="utf-8") as f:
    long_description = f.read()

setup(
  name = 'hatebase',
  packages = ['hatebase'],
  package_dir = {'hatebase': 'hatebase'},
  package_data = {'hatebase': ['__init__.py', 'tests/__init__.py', 'tests/test.py']},
  version = '1.0.3',
  description = "Python Version of Andrew Welter's Hatebase Wrapper, based on DanielJDufour's implementation",
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Daniel J. Dufour & Alexander Meier',
  author_email = 'daniel.j.dufour@gmail.com',
  url = 'https://github.com/DanielJDufour/hatebase',
  download_url = 'https://github.com/DanielJDufour/hatebase/tarball/download',
  keywords = ['conflict', 'hatespeech', 'language', 'nlp', 'python', 'tagging'],
  classifiers = [],
  install_requires=["requests"]
)
