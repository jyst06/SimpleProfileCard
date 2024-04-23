from setuptools import setup, find_packages

setup(
    name='profilecard',
    version='1.0.3',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.ini']},
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
)
