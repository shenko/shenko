# We based shenko docker on Ubuntu (18.04)
# At a minimum running this should give you shenko fob
# LAN for free or WAN at www.shenko.org for more information

FROM        ubuntu:18.04
MAINTAINER  shenko.org <shenko.org@gmail.com>

# https://Gitub.com/shenko/shenko Last build build
# date: Feb 21, 2019
# version: version='0.1.12'
# Git Hash:
# 564819edbe6a696c6fbfc6fbaf264bfd4a7c71bb

ENV         security_updates_as_of 2018-02-21

# Install security updates and required packages
RUN         apt-get update && \
            apt-get -y upgrade && \
            apt-get -y install -q build-essential && \
            apt-get -y install -q python-dev libffi-dev libssl-dev python-pip
#           #Todo:
#            wget -O - http://shenko.org/index.php/downloads/ | wc -l > /number
#            set -o pipefail && wget -O - https://some.site | wc -l > /number

# Install required python packages, and librairies[shenko, twisted, panda3d]
RUN         pip install service_identity pycrypto && \
#            pip install twisted==14.0.0
            pip install shenko

#CMD ["bash"]            
CMD ["shenko"]

