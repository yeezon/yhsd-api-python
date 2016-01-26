# -*- coding: utf-8 -*-
# !/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='yhsd-sdk',
    version='1.0.0',
    keywords=('yhsd', 'sdk', 'yhsd sdk'),
    description=u'友好速搭应用Python开发包',
    long_description=open("README.md").read(),
    license='BSD License',
    # change to your own url
    #url='http://git.yingxuan.io/yingxuan/a16398',
    author='charlie',
    author_email='charlie.szu@qq.com',

    packages=find_packages(),
    include_package_data=True,
    install_requires=map(lambda x: x.replace('==', '>='), open("requirements.txt").readlines()),
)
