import os
from setuptools import find_packages, setup
from .version import get_version

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='project',
    version=get_version(),
    packages=find_packages(),
    scripts=['manage.py'],
    )
