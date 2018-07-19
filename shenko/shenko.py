#!/usr/bin/env python
# -*- coding: utf-8 -*-
#FILE:          main.py
#SOURCE:        viper/system/core/
__author__      = "Danny Dowshenko"
__copyright__   = "http://creativecommons.org/licenses/by/3.0/legalcode"
#DESCRIPTION: 
"""
MAIN MENU that threads
    -each 'core' element is a thread
    -main listens to 'core'
"""

import 01_HOME
import 02_FILESYSTEM
import 03_TEMPORARY
import 04_INPUTS
import 05_CENTRAL
import 06_OUTPUT
import 07_ROBOT_HOME
import 08_NETWORK
import 09_EXTERNAL


#-------------SYNOPSIS------------------/
"""

"""

#--------------VARIABLES---------------/

#--------------FUNCTIONS---------------/

#----------------MAIN------------------/

def main():
    print "main core is running"
    S_00_ROBOT_HOME.ROBOT_HOME()
    S_01_HOME.HOME()
    S_02_FILESYSTEM.FILESYSTEM()
    S_03_TEMPORARY.TEMPORARY()
    S_04_INPUTS.INPUTS()
    S_05_CENTRAL.CENTRAL()
    S_06_OUTPUT.OUTPUT()
    S_07_PSU.PSU()
    S_08_NETWORK.NETWORK()
    S_09_EXTERNAL.EXTERNAL()

# For making modules"
if __name__ == '__main__':
    main()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    print " " 

