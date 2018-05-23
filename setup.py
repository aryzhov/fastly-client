from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="fastly-client",
    version="0.1.7",
    author="Alexander Ryzhov",
    author_email="aryzhov07@gmail.com",
    description=("Fastly API client that supports billing and stats."),
    license="MIT",
    keywords="fastly api billing stats client",
    url="https://github.com/aryzhov/fastly-client",
    packages=find_packages(exclude=['test']),
    install_requires=[
        'marshmallow >= 3.0.0b11',
        'requests >= 2.18.4'
    ],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
