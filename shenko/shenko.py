#!/usr/bin/env python
# -*- coding: utf-8 -*-
#FILE:          main.py
#SOURCE:        viper/system/core/
__author__      = "Danny Dowshenko"
__copyright__   = "http://creativecommons.org/licenses/by/3.0/legalcode"
#DESCRIPTION: 
"""
# MAIN MENU that threads
    -each 'core' element is a thread
    -main listens to 'core'
"""

from S01_HOME.HOME import home
from S02_FILESYSTEM.FILESYSTEM import filesystem
from S03_TEMPORARY.TEMPORARY import temporary
from S04_INPUTS.INPUTS import inputs
from S05_CENTRAL.CENTRAL import central
from S06_OUTPUT.OUTPUT import output
from S07_ROBOT_HOME.ROBOT_HOME import robotHome
from S08_NETWORK.NETWORK import network
from S09_EXTERNAL.EXTERNAL import external

#-------------SYNOPSIS------------------/
#--------------VARIABLES---------------/
#--------------FUNCTIONS---------------/
#----------------MAIN------------------/

def main():
    print("main core is running")
    home()
    filesystem()
    temporary()
    inputs()
    central()
    output()
    robotHome()
    network()
    external()

# For making modules"
if __name__ == '__main__':
    main()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    print("importing main") 

