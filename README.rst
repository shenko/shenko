
# WELCOME TO SHENKO
## Installing Shenko

### Windows and macOS Users ###

To install Shenko, download the appropriate package from our website at [www.shenko.org].(https://www.shenko.org/downloads) Here you will find them already bundled for easy installation on your platform

---

### Linux Users

#### Method 1: Cloning the repository directly from GitHub ####

To get the latest development version of Shenko, you can clone the repository from GitHub:

        git clone https://github.com/shenko/shenko.git
        cd shenko
        pip3 install -r requirements.txt

*This method allows you to access the latest code and contribute to development if desired. Our about page will have detailed instructions if you want to join our team of developers.*

#### Method 2: Downloading the tarball from our website ####

You can download the .tar.gz package for Linux from our website:
    1. Visit www.shenko.org/download
    2. Download the .tar.gz package.
    3. Extract it: tar -xvzf shenko-x.y.z.tar.gz
    4. Run the game: cd shenko && ./shenko.py
    *You may need to make it executable with 'chmod +x shenko.py'

#### Method 3: Other Formats (**Coming Soon in v0.2**) ####

Using the 'apt' command from a terminal 
        sudo add-apt-repository ppa:shenko/ppa
        sudo apt-get update
        sudo apt-get install shenko
*Canonical site that hosts the repository* 

Using the 'snap' package manager:
        \# Install snap package manager (if needed)
        sudo apt update
        sudo apt install snapd

        sudo snap install shenko
[Launchpad.net](https://launchpad.net/~shenko)
[![shenko](https://snapcraft.io/shenko/badge.svg)](https://snapcraft.io/shenko)

Using Docker:
        # Install Docker:
        sudo apt update
        sudo apt install docker.io

        # Start and enable Docker service:
        sudo systemctl start docker
        sudo systemctl enable docker

        # Verify Docker installation:
        docker --version

        # Pull the Shenko Docker Image:
        docker pull shenko/shenko.docker

        # Run Shenko in a Docker Container:
        docker run -it shenko/shenko.docker

        # To STOP the running Shenko Container:
        docker stop <container_id>

*Shenko's official Docker page.* [hub.docker.com](https://hub.docker.com/r/shenko/shenko.docker)
[![Docker Image Version](https://img.shields.io/docker/v/shenko/shenko.docker?color=green)](https://hub.docker.com/r/shenko/shenko.docker)
[![Docker Pulls](https://img.shields.io/docker/pulls/shenko/shenko.docker?color=green)](https://hub.docker.com/r/shenko/shenko.docker)
[![Docker Image Size](https://img.shields.io/docker/image-size/shenko/shenko.docker?color=green)](https://hub.docker.com/r/shenko/shenko.docker)

### From PyPI

As of Ubuntu 23.04 the pip install method will no longer be supported
as if conflicts with a change in policy to avoid conflicts between
the Python package manager(pip) and Ubuntu's underlying APT. 
*You can still use pipby creating a virtual environment with vent.

Install the latest development build of Shenko using the following command:

        # Clone the shenko repository on GitHub
        git clone git@github.com:shenko/shenko.git

        # Setup a virtual Environment
        mkvirtualenv shenko
        cd shenko/
        python setup.py develop

        # Create a branch to develop on
        git checkout -b name-of-your-bugfix-or-feature

        # Run it through a barrage of tests
        flake8 shenko tests
        python setup.py test  # or py.test
        tox
        *if not already installed 'pip install tox flake8'*

        # Commit your changes and push your branch to GitHub:
        git add .
        git commit -m "Your detailed description of your changes."
        git push origin name-of-your-bugfix-or-feature

.. image:: https://img.shields.io/pypi/v/shenko.svg
        :target: https://pypi.python.org/pypi/shenko

## Getting Help and Additional Documentation

For detailed documentation on Shenko, including usage instructions, setup guides, and troubleshooting tips, please visit our [Documentation](https://shenko.readthedocs.io/en/latest/). 

![Documentation Status](https://readthedocs.org/projects/shenko/badge/?version=latest)

If you have any questions or need further assistance, feel free to visit our [About page](https://shenko.org/about) on our website. This page includes frequently asked questions, contact information, and additional support resources.

Should you encounter any issues or need specific help related to Shenko, our community is here to assist you. Don't hesitate to reach out or check the available documentation for more insights.

## Usage

This project is Licensed under:
* Free software: GNU General Public License v3

We are still in the early stages of development,
The best way to see our latest developments is to
visit www.shenko.org or follow us on social media

## Features

This project is written entirely in python, and
uses the panda3d game engine.
