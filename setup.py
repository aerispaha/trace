import os
from setuptools import setup, find_packages
import ast

HERE = os.path.abspath(os.path.dirname(__file__))


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_description():
    """Get long description."""
    with open(os.path.join(HERE, 'README.md'), 'r') as f:
        data = f.read()
    return data


def get_version(module='sewergraph'):
    """Get version."""
    with open(os.path.join(HERE, module, '__init__.py'), 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('VERSION_INFO'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version


REQUIREMENTS = [
    'pandas',
    'networkx>=2',
    'numpy',
    ]


setup(name='sewergraph',
      version=get_version(),
      description='Tools for graph calculations on sewer networks',
      author='Adam Erispaha',
      url='https://github.com/aerispaha/sewergraph',
      author_email='aerispaha@gmail.com',
      packages=find_packages(exclude=('tests')),
      install_requires=REQUIREMENTS,
      long_description=get_description(),
      long_description_content_type="text/markdown",
      platforms="OS Independent",
      license="MIT License",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.6",
      ]
)
