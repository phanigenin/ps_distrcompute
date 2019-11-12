from setuptools import setup, find_packages

setup(
    name='ps_distrcompute',
    version='0.1.0',
    description='All distributed compute utilities',
    long_description='MultiThreading, Multiprocessing and datasynapse',
    author='Phani Sarma',
    author_email='phani.mfe@gmail.com',
    url='https://github.com/phanigenin',
    install_requires=['concurrent'],
    packages=find_packages(exclude=('docs'))
)