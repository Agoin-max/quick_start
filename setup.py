# setup.py

from setuptools import setup, find_packages

setup(
    name="calculator-double",
    version="0.1",
    packages=find_packages(),
    py_modules=["calculator"],
    entry_points={
        "console_scripts": [
            "calculate=calculator:main",
        ],
    },
    # metadata to display on PyPI
    author="luofuwen",
    author_email="your.email@example.com",
    description="A simple calculator package",
    keywords="calculator, addition",
    url="https://github.com/Agoin-max/quick_start",
    project_urls={
        "Source Code": "https://github.com/Agoin-max/quick_start",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
