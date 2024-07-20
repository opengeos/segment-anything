# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Qiusheng Wu",
    author_email="giswqs@gmail.com",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="An unofficial Python package for Meta AI's Segment Anything Model",
    url="https://github.com/opengeos/segment-anything",
    name="segment-anything-py",
    version="1.0.1",
    install_requires=["torch>=1.7", "torchvision>=0.8"],
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude="notebooks"),
    extras_require={
        "all": ["matplotlib", "pycocotools", "opencv-python", "onnx", "onnxruntime"],
        "dev": ["flake8", "isort", "black", "mypy"],
    },
)
