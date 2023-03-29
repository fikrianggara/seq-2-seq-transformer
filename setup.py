import sys
import setuptools
from pipenv import project, utils

#pipenv version >= 2022.4.8
pipfile = project.Project().parsed_pipfile
packages = pipfile["packages"].copy()
requirements = utils.dependencies.convert_deps_to_pip(packages, )

setuptools.setup(
    packages=setuptools.find_packages(),
    install_requires=requirements
)