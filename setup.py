from distutils.core import setup

setup(
  name = 'hatebase',
  packages = ['hatebase'],
  package_dir = {'hatebase': 'hatebase'},
  package_data = {'hatebase': ['__init__.py', 'tests/__init__.py', 'tests/test.py']},
  version = '0.4',
  description = "Python Version of Andrew Welter's Hatebase Wrapper",
  author = 'Daniel J. Dufour',
  author_email = 'daniel.j.dufour@gmail.com',
  url = 'https://github.com/DanielJDufour/hatebase',
  download_url = 'https://github.com/DanielJDufour/hatebase/tarball/download',
  keywords = ['conflict', 'hatespeech', 'language', 'nlp', 'python', 'tagging'],
  classifiers = [],
  install_requires=["requests"]
)
