from setuptools import setup, find_packages

setup(
    name="mcsmod",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pandas==1.2.4',
        'numpy==1.19.5'
    ],
)