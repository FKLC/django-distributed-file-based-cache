import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-distributed-file-based-cache",
    version="1.0.3",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    description="A simple Django app to sync file caches over all nodes.",
    long_description=README,
    author="Fatih Kılıç",
    author_email="m.fatihklc0@gmail.com",
    url="https://github.com/FKLC/django-distributed-file-based-cache",
    download_url="https://pypi.org/project/django-distributed-file-based-cache/",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=["django-serviceless-distributor"],
)
