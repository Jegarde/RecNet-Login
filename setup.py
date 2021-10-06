from setuptools import setup
import re

setup(
    name='recnetlogin',
    author='Jegarde',
    url='https://github.com/Jegarde/RecNet-Login/',
    version=0.1,
    packages=['recnetlogin'],
    license='MIT',
    description='A package that allows you to acquire a bearer token from RecNet with account credentials.',
    install_requires=['requests==2.25.1'],
    python_requires='>=3.9.0'
)
