from setuptools import setup

"""
	pigeon/
	|-- README
	|-- setup.py
	|-- pigeon
	|   |-- __init__.py
	|   |-- pigeon.py

"""

setup(
    name = "pigeon",
    version = "0.0.1",
    author = "Radu Nicolae",
    author_email = "ranicolae@gmail.com",
    description = ("JSON based, config object. Includes schema validation"),
    license = "MIT",
    keywords = "config configuration json validation",
    url = "https://github.com/RadRobot/pigeon",
    packages=['pigeon']
)
