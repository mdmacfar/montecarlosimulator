from setuptools import setup, find_packages

setup(
    name="mcs",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pandas==1.2.4',
        'numpy==1.19.5'
    ],
    author="Michael Macfarlan",
    description="Monte Carlo Simulator",
    url="https://github.com/mdmacfar/montecarlosimulatormodule",
)