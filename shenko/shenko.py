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
"""

"""

#--------------VARIABLES---------------/

#--------------FUNCTIONS---------------/

#----------------MAIN------------------/

def main():
    print "main core is running"
    S01_HOME.HOME()
    S02_FILESYSTEM.FILESYSTEM()
    S03_TEMPORARY.TEMPORARY()
    S04_INPUTS.INPUTS()
    S05_CENTRAL.CENTRAL()
    S06_OUTPUT.OUTPUT()
    S07_ROBOT_HOME.ROBOT_HOME()
    S08_NETWORK.NETWORK()
    S09_EXTERNAL.EXTERNAL()

# For making modules"
if __name__ == '__main__':
    main()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    print " " 

