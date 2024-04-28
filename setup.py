from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='profilecard',
    version='1.0.8',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    package_data={'': ['*.ini']},
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
)
