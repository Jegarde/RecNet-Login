from setuptools import setup
import re

setup(
    name='recnetlogin',
    author='Jegarde',
    url='https://github.com/Jegarde/RecNet-Login/',
    version=1.0,
    packages=['recnetlogin'],
    license='MIT',
    description='A Python package, that allows you to acquire your RecNet authorization bearer token with your account credentials!',
    install_requires=[
        "aiodns==3.0.0",
        "aiohttp==3.8.1",
        "aiosignal==1.2.0",
        "async-timeout==4.0.2",
        "attrs==21.4.0",
        "beautifulsoup4==4.10.0",
        "Brotli==1.0.9",
        "bs4==0.0.1",
        "cchardet==2.1.7",
        "certifi==2021.10.8",
        "cffi==1.15.0",
        "charset-normalizer==2.0.12",
        "frozenlist==1.3.0",
        "idna==3.3",
        "multidict==6.0.2",
        "pycares==4.1.2",
        "pycparser==2.21",
        "PyJWT==2.3.0",
        "requests==2.27.1",
        "soupsieve==2.3.1",
        "urllib3==1.26.8",
        "yarl==1.7.2"
    ],
    python_requires='>=3.8.0'
)
