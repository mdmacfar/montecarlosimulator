from setuptools import setup, find_packages

setup(
    name="Monte Carlo Simulator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=['pandas'],
    author="Michael Macfarlan",
    description="Monte Carlo Simulator package containing Die, Game, and Analyzer classes",
    url="https://github.com/mdmacfar/montecarlosimulator",
    license="MIT"
)