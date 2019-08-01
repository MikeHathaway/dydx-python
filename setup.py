import os
from setuptools import setup, find_packages


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
REQUIREMENTS = [
     'requests>=2.5',	README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
    'six==1.12',
    'web3==4.9.2',
    'pytest>=4.4.0,<5.0.0',
    'tox==3.13.2',
    'setuptools',
    'eth_keys'
]

setup(
    name='dydx-python',
    version='0.0.3',
    packages=find_packages(),
    description='dYdX Python REST API for Limit Orders',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/dydxprotocol/dydx-python',
    author='dYdX Trading Inc.',
    license='Apache 2.0',
    author_email='contact@dydx.exchange',
    install_requires=REQUIREMENTS,
    keywords='dydx exchange rest api defi ethereum eth',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
