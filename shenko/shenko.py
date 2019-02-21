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
"""
import S01_HOME
import S02_FILESYSTEM
import S03_TEMPORARY
import S04_INPUTS
import S05_CENTRAL
import S06_OUTPUT
import S07_ROBOT_HOME
import S08_NETWORK
import S09_EXTERNAL

#-------------SYNOPSIS------------------/
#--------------VARIABLES---------------/
#--------------FUNCTIONS---------------/
#----------------MAIN------------------/

def main():
    print("main core is running")
    S01_HOME.home()
    S02_FILESYSTEM.filesystem()
    S03_TEMPORARY.temporary()
    S04_INPUTS.inputs()
    S05_CENTRAL.central()
    S06_OUTPUT.output()
    S07_ROBOT_HOME.robotHome()
    S08_NETWORK.network()
    S09_EXTERNAL.external()

# For making modules"
if __name__ == '__main__':
    main()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    print("importing main") 

