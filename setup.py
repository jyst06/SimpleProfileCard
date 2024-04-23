from setuptools import setup, find_packages

setup(
    name='profilecard',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
)