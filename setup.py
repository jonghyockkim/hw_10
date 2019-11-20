#!/usr/bin/env python
from setuptools import setup
setup(
    name="jong_package",
    version="0.2",
    scripts=["hw_9.py"],
    data_files = [('.', ['test1112.csv'])],
    install_requires=['matplotlib', 'pandas'],
    author="Jong Kim",
    author_email="jonghyockkim@naver.com",
    description="This is an Example Package.. It might not work...",
    keywords="hw_9 is clustering example",
    url="http://example.com/HelloWorld/",   
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://code.example.com/HelloWorld/",
    },
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]

)
