# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup


base_dir = os.path.dirname(__file__)

setup(
    name='Notifikator',
    version='0.1.2',
    description='Notifikator is a RESTful notification service for Elasticsearch.',
    author='Markus Schneider',
    author_email='markus.schneider73@gmail.com',
    setup_requires='setuptools',
    license='Copyright 2020 Markus Schneider',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: BSD 3-Clause License'
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    install_requires=[
        'flask==1.1.2',
        'elasticsearch==7.9.1',
        'click==7.1.2',
        'pytest==5.4.2',
        'gunicorn==20.0.4',
        'requests==2.24.0'
    ]
)
