from setuptools import setup, find_packages

NAME = "odin-cyble"
VERSION = "0.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23",
    "requests>=2.0"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="ODIN APIs",
    author_email="Anukul Kumar <anukul.kumar@cyble.com>",
    url="",
    keywords=["ODIN SDK", "ODIN APIs"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    APIs fetchs the data based on query 
    """
)
