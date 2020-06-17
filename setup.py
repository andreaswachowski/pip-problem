import pip
from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements
from setuptools import find_packages, setup

install_requires_g = parse_requirements("requirements.txt", session=PipSession())

if tuple(map(int, pip.__version__.split("."))) >= (20, 1):
    install_requires = [str(ir.requirement) for ir in install_requires_g]
else:
    install_requires = [str(ir.req) for ir in install_requires_g]

setup(
    name="pkg",
    install_requires=install_requires,
    version="0.1.0",
    packages=find_packages(),
)
