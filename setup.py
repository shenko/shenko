# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    #'platform>=3.9.1'
    'Click>=6.0',
    'panda3d>=1.10.10',
    # TODO: Put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(shenko): Put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: Put package test requirements here
    # 		do we need to add 'unitest'???
]

setup(
    name='shenko',
    version='0.1.60',
    description="visit us at www.shenko.org",
    long_description=readme + '\n\n' + history,
    author="Danny Dowshenko",
    author_email='dowshenko225@gmail.com',
    url='https://github.com/shenko/shenko',
    packages=find_packages(where='shenko',
        include=['shenko.S01_HOME'],
    ),
    # entry_point runs a script, let's try and skip this
    #entry_points={
    #    'console_scripts': [
    #        'shenko = shenko.shenko:main',
    #    ],
    #},
    #
    # This was the old entry point to run shenko as command line
    #entry_points={
    #    'console_scripts': [
    #        'shenko=shenko.cli:main',
    #    ],
    #},
    include_package_data=True,
    package_data={'shenko': ['*.ogg', 'logo.png']},
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='shenko',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        #"Programming Language :: Python :: 2",
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
