from setuptools import setup, find_packages

setup(
    name='profilecard',
    version='1.0.3',
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    package_data={'': ['*.ini']},
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
)
