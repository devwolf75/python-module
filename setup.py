import io
import sys
import os

from setuptools import setup, find_packages

import about_vars

HERE = os.curdir
PACKAGE = os.path.join(HERE, about_vars.package_name)

with io.open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with io.open("LICENSE.md", "r", encoding="utf-8") as license_file:
    license_f = license_file.read()

with io.open("requirements.txt", "r", encoding="utf-8") as require:
    requires = require.read().splitlines()

with io.open("test_requirements.txt", "r", encoding="utf-8") as test_require:
    test_requires = test_require.read().splitlines()

if sys.argv[-1] == "readme":
    print(readme)
    sys.exit()


def find_packages_by_root_package(where):
    root_package = os.path.basename(where)
    packages = [
        "%s.%s" % (root_package, sub_package) for sub_package in find_packages(where)
    ]
    packages.insert(0, root_package)
    return packages


setup(
    name=about_vars.package_name,
    version=about_vars.version,
    author=about_vars.author,
    author_email=about_vars.author_email,
    maintainer=about_vars.maintainer,
    maintainer_email=about_vars.maintainer_email,
    description="Package short description here.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://documentation.com",
    packages=find_packages_by_root_package(PACKAGE),
    install_requires=requires,
    test_require=test_require,
    include_package_data=True,
    python_requires=">3.9",
    license=license_f,
)
