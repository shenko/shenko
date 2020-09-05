#!/usr/bin/env python
# -*- coding: utf-8 -*-
#FILE:          main.py
#SOURCE:        https://github.com/shenko/shenko/blob/master/shenko/shenko.py
__author__      = "Danny Dowshenko"
__copyright__   = "http://creativecommons.org/licenses/by/3.0/legalcode"
#DESCRIPTION:
"""
# MAIN MENU that threads
    -each 'core' element is a thread
    -main listens to 'core'
"""
import sys
import os
import time

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
https://docs.panda3d.org/1.10/python/programming/tasks-and-events/tasks

# I think the only way to solve our dilema is to put a
# listner on CENTRAL
# and putter on every other node
"""
#--------------VARIABLES---------------/
shareme = True
#--------------INIT FUNCTIONS---------------/


#----------------MAIN------------------/
def main():
    print("main core is running!!!")
    S01_HOME.home()
    S02_FILESYSTEM.filesystem()
    S03_TEMPORARY.temporary()
    S04_INPUTS.Keyboard(shareme)
    app = S05_CENTRAL.MyApp()
    S06_OUTPUT.output()
    S07_ROBOT_HOME.robotHome()
    S08_NETWORK.network()
    S09_EXTERNAL.external()

    # Run is just Task.step() looped
    #app = MyApp()
    app.run()

# For making modules"
if __name__ == '__main__':
    print('main.py is being run directly')
    main()
else:
    print("main.py is being imported")
    print("shenko/shenko/shenko.py importing main")
    main()
