"""A setuptools based setup module for easycalc.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    
    name='easycalc',  # Required

    version='1.0.1',  # Required
    description='A very easy calculator for command line',  # Required
    #long_description=long_description,  # Optional

    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url='https://github.com/lruzicka/pythonprogs/tree/master/easycalc',  # Optional

    # This should be your name or the name of the organization which owns the
    # project.
    author='Lukas Ruzicka',  # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='lukas.ruzicka@gmail.com',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],

    keywords='calculator simple limited',  # Optional

    #
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    #install_requires=['peppercorn'],  # Optional

    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'easycalc=easycalc:main',
        ],
    },
)

