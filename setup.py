# coding=utf-8
# Copyright 2025 the SmallDoge team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import shutil
from pathlib import Path

from setuptools import find_packages, setup

__version__ = "0.1.0"

# Remove stale small_doge.egg-info directory to avoid https://github.com/pypa/pip/issues/5466
stale_egg_info = Path(__file__).parent / "small_doge.egg-info"
if stale_egg_info.exists():
    print(
        (
            "Warning: {} exists.\n\n"
            "If you recently updated small_doge, this is expected,\n"
            "but it may prevent small_doge from installing in editable mode.\n\n"
            "This directory is automatically generated by Python's packaging tools.\n"
            "I will remove it now.\n\n"
            "See https://github.com/pypa/pip/issues/5466 for details.\n"
        ).format(stale_egg_info)
    )
    shutil.rmtree(stale_egg_info)


setup(
    name="small_thoughts",
    license="Apache-2.0",
    version="0.1.0",
    description="Distill thinking dataset more compactly and accurately!",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="The SmallDoge Team",
    author_email="losercheems@gmail.com",
    url="https://github.com/SmallDoges/small-thoughts",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "datasets>=3.0.2",
        "timeout-decorator>=0.5.0",
        "rapidfuzz>=3.11.0",
        "bespokelabs-curator>=0.1.16",
        "math-verify>=0.3.2",
    ],
    extras_require={
        "dev": [
            "twine>=5.0.0",
            "ruff>=0.8.6",
            "isort>=5.13.2",
            "pre-commit>=4.0.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "curator-viewer=bespokelabs.curator.viewer.__main__:main",
        ],
    },
    keywords=["small-thoughts", "distill", "thinking", "dataset"],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)