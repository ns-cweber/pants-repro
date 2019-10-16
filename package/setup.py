import os

import setuptools

setuptools.setup(
    name="package",
    version=os.environ.get("BUILD_VERSION", "0.0.0.dev-1"),
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    provides=setuptools.find_packages("src"),
    dependency_links=[],
    entry_points={"console_scripts": ["main=main.main:main"]},
)
