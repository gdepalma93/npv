#! /usr/bin/env python

import os

DESCRIPTION = "Net Present Value Simulator for Python"
LONG_DESCRIPTION = """\
npv.py An NPV Simulator for Python
==============================================
**npv.py** is a Python package that provides a
high performance, easy-to-use facility for
simulating any number of NPV outcomes for a given
business model.
"""

DISTNAME = 'npv'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://github.com/mikkokotila'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/mikkokotila/npvpy'
VERSION = '0.4.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup


def check_dependencies():
    install_requires = []

    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')

    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')

    #try:
    #    import seaborn
    #except ImportError:
    #    install_requires.append('seaborn')

    try:
        import matplotlib
    except ImportError:
        install_requires.append('matplotlib')

    return install_requires


if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['npvpy'],
          classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
          )
