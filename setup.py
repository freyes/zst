from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zst',
    version='0.1',
    description='Check status of a job in zuul',
    url='https://github.com/freyes/zst',
    author='Felipe Reyes',
    author_email='freyes@tty.cl',
    license='GPLv2+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    keywords='zuul',
    py_modules=["zst"],
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'zst=zst:main',
        ],
    },
)
