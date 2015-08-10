#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='django-datatables-views',
    version='0.2',
    description='CBV to create fast table views based on datatables.js',
    author='a1fred',
    author_email='demalf@gmail.com',
    license='MIT',
    url='https://github.com/a1fred/django-datatables-views',
    packages=['datatables_views'],
    platforms=['any'],
    zip_safe=False,
    install_requires = [
        'django>=1.4',
    ],
    )
