import os.path
import sys

sys.path.insert(0, os.path.abspath('lib'))

try:
    from setuptools import setup, find_packages
except ImportError:
    sys.exit(1)


with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name='tarsier-input-webapi',
    version="0.1.0",
    package_dir={'': 'lib'},
    packages=find_packages('lib'),
    author="Hiroki Mizumoto",
    author_email="shuibenhonggui@gmail.com",
    url="https://github.com/motomizuki/tarsier-input-webapi",
    description="Webapi input plugin for tarsier",
    license="MIT License",
    install_requires=install_requirements,
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
