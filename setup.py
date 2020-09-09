"""Setup script."""
#!/usr/bin/env python
from setuptools import setup

version = __import__('pysumtypes').__version__

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    author='Dan Pozmanter',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description='Sum Types for Python',
    keywords='sumtypes adt discriminatedunions uniontypes algebraicdatatypes',
    license='BSD',
    long_description=long_description,
    name='PySumTypes',
    packages=['pysumtypes'],
    url='https://github.com/danpozmanter/PySumTypes',
    version=version,
    zip_safe=False,
)
