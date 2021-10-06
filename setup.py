from setuptools import setup
import re

version = ''
with open('recnetlogin/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("Version isn't set!")

setup(
    name='recnetlogin',
    author='Jegarde',
    url='https://github.com/Jegarde/RecNet-Login/',
    version=version,
    packages=['recnetlogin'],
    license='MIT',
    description='A package that allows you to acquire a bearer token from RecNet with account credentials.',
    install_requires=['requests==2.25.1'],
    python_requires='>=3.9.0'
)
