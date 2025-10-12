# Shenko Docker on Ubuntu
# visit us at www.shenko.org for more information
FROM        ubuntu:24.04
MAINTAINER  shenko.org <shenko.org@gmail.com>

# Updated: October 2025
# version='0.1.90'
# Python: 3.12

ENV         DEBIAN_FRONTEND=noninteractive
ENV         security_updates_as_of 2025-10-11

# Install security updates and required packages
RUN         apt-get update && \
            apt-get -y upgrade && \
            apt-get -y install -q \
                build-essential \
                python3.12 \
                python3.12-dev \
                python3-pip \
                python3-venv \
                libffi-dev \
                libssl-dev \
                git \
                wget \
                curl && \
            apt-get clean && \
            rm -rf /var/lib/apt/lists/*

# Set Python 3.12 as default python3
RUN         update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1

# Upgrade pip
RUN         python3 -m pip install --break-system-packages --upgrade --ignore-installed pip setuptools wheel

# Copy requirements file
COPY        requirements.txt /tmp/requirements.txt

# Install Python dependencies
RUN         pip install --break-system-packages --no-cache-dir -r /tmp/requirements.txt

# Install shenko package
# Option 1: Install from PyPI (after you publish)
RUN         pip install --break-system-packages --no-cache-dir shenko

# Option 2: Install from local source (uncomment if building from source)
# COPY        . /app
# WORKDIR     /app
# RUN         pip install --no-cache-dir -e .

# Set working directory
WORKDIR     /app

# Expose ports if needed for multiplayer server
# EXPOSE      6667
# EXPOSE      7099

# Default command
CMD         ["shenko"]
