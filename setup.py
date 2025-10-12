# -*- coding: utf-8 -*-
# version="0.1.86"
"""
The setup script.

Build commands:
    python3 -m build              # Build both source and wheel distributions
    python3 -m build --sdist      # Build only source distribution
    python3 -m build --wheel      # Build only wheel distribution

Upload workflow:
    # 1. Check distributions are valid
    twine check dist/*
    
    # 2. Test upload to TestPyPI (optional but recommended)
    twine upload --repository testpypi dist/*
    
    # 3. Upload to PyPI
    twine upload dist/*
    
    # Or upload specific version
    twine upload dist/shenko-0.1.86*

Panda3D standalone builds:
    python setup.py build_apps    # Build standalone executables for all platforms
    
    Outputs to build/ directory:
    - Linux: manylinux2014_x86_64/
    - macOS: macosx_10_9_x86_64/
    - Windows: win_amd64/

Docker builds:
    docker build -t shenko:latest .           # Build Docker image
    docker run -it shenko:latest              # Run container
    docker run -it shenko:latest /bin/bash    # Interactive shell
    
    # For local development (mount source code)
    docker build -t shenko:dev -f Dockerfile.dev .
    docker run -it -v $(pwd):/app shenko:dev

Prerequisites:
    pip install build twine       # Install build and upload tools
    docker                        # For Docker builds
"""

# don't need find_packages for panda3d I'm pretty sure I read that
from setuptools import setup, find_packages
import os
import glob
import re

# Import version from _version.py
with open('_version.py', 'r') as f:
    version_file = f.read()

version_match = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", version_file)
if version_match:
    version = version_match.group(1)
else:
    raise RuntimeError('Unable to find version string in _version.py')

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
    version=version,
    description="visit us at www.shenko.org",
    long_description=readme + '\n\n' + history,
    author='Shenko Development Team',
    author_email='shenko.org@gmail.com',
    url='https://github.com/shenko/shenko',
    packages=find_packages(include=['shenko',
                                    'shenko.*'
                                    ]),
    include_package_data=True,
    entry_points={
        'gui_apps': [
            'shenko = shenko.shenko:main',
        ],
    },
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
            # TODO: Re-enable asset patterns once asset directory structure is resolved
            # 'include_patterns': [
            #     '**/*.png',
            #     '**/*.jpg',
            #     '**/*.gltf',
            #     '**/*.glb',
            #     '**/*.egg.pz',
            #     '**/*.blend',
            #     '**/*.ogg',
            #     '**/*.wav'
            # ],
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
