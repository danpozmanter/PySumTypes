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
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description='Sum Types for Python',
    keywords='sumtypes adt discriminatedunions uniontypes algebraicdatatypes',
    license='BSD',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='PySumTypes',
    packages=['pysumtypes'],
    python_requires='>=3.7',
    url='https://github.com/danpozmanter/PySumTypes',
    version=version,
    zip_safe=False,
)
