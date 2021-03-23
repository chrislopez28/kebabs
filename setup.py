import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="kebabs",
    version="1.0.0",
    description="Convert a string to kebab-case",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/chrislopez28/kebabs",
    author="Chris Lopez",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["kebabs"],
)
