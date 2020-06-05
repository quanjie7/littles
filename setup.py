# -*- coding: utf-8 -*-
# @Time: 2020/5/15 11:54
import setuptools

with open("Readme.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="littles",
    version="0.1.1",
    author="quanjie",
    author_email="iquanjie@foxmail.com",
    description="a little tool for python;python编程中的一些常用小工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
