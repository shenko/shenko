# -*- coding: utf-8 -*-

"""The setup script."""

# don't need find_packages for panda3d I'm pretty sure I read that
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
    version='0.1.83',
    description="visit us at www.shenko.org",
    long_description=readme + '\n\n' + history,
    author='Shenko Development Team',
    author_email='shenko.org@gmail.com',
    url='https://github.com/shenko/shenko',
    packages=find_packages(include=['shenko',
                                    'shenko.s00_init'
                                    ]),
    entry_points={
        'gui_apps': [
            'shenko = shenko.shenko:main',
        ],
    },
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
    options={
        'build_apps': {
            # Build a GUI application
            'gui_apps': {
                'shenko': 'shenko/shenko.py',
            },
            # Set up output logging, important for GUI apps!
            'log_filename': '$USER_APPDATA/shenko/output.log',
            'log_append': False,
            # Specify which files are included with the distribution
            'include_patterns': [
                '**/*.png',
                '**/*.jpg',
                '**/*.gltf',
            ],
            # Include the OpenGL renderer and OpenAL audio plug-in
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],
            'platforms': [
                'manylinux2014_x86_64',
                'macosx_10_9_x86_64',
                'win_amd64',
            ],
        }
    }
)
