from setuptools import setup

from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
# test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)

setup(
    name='xsd2json',
    version='0.1.0',
    description='Convert XSD to JSON Schema',
    author='Ben Scott',
    maintainer='dhilipsiva'
    author_email='ben@benscott.co.uk',
    maintainer_email='dhilipsiva@gmail.com'
    packages=['xsd2json'],
    install_requires=requirements,
    entry_points={
        'console_scripts': ['xsdtojson=xsdtojson.cli:main'],
    }
)
