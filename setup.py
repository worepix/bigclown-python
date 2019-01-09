from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read()

setup(
    name='bigclown',
    packages=find_packages('bigclown'),
    package_dir={'': 'bigclown'},
    include_package_data=True,
    version='@@VERSION@@',
    description='Python libary for Python',
    url='https://github.com/worepix/bigclown-python',
    author='BigClown',
    author_email='ask@bigclown.com',
    license='MIT',
    keywords = ['bigclown', 'libary', 'iot'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Environment :: Plugins',
        'Intended Audience :: Developers'
    ],
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown'
)