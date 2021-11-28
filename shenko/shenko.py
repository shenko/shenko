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

# To be tested:
After installing with pip, the path to my dirs seems to not registered
with the 'clients' $PATH so I get something like missing S01_HOME

To get the full path to the directory a Python file is contained in,
write this in that file:

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

"""
import sys
import os
import time
import platform

#import S01_HOME
#import S02_FILESYSTEM
#import S03_TEMPORARY
#import S04_INPUTS
#import S05_CENTRAL
#import S06_OUTPUT
#import S07_ROBOT_HOME
#import S08_NETWORK
#import S09_EXTERNAL

import S01_HOME.HOME

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText

#-------------SYNOPSIS------------------/
"""
https://docs.panda3d.org/1.10/python/programming/tasks-and-events/tasks

# I think the only way to solve our dilema is to put a
# listner on CENTRAL
# and putter on every other node
"""
#--------------VARIABLES---------------/
mainMenuState = True
cameraActive = []     # if list is empty it is 'false'
#--------------INIT FUNCTIONS---------------/
# When Shenko installs with pip, this will add this folder to client's path
#dir_path = os.path.dirname(os.path.realpath(__file__))

def setupSequence():
    print(os.listdir("."))
    print(os.getcwd())
    # I want to know where to download Shenko Models/Assets
    # It may be different on certain platforms
    plt = platform.system()

    if plt == "Windows":
        print("Your system is Windows")
        # create a users 'workspace' in C:\
    elif plt == "Linux":
        print("Your system is Linux")
        # create a user 'workspace' in /home/$USER/$workspace
    elif plt == "Darwin":
        print("Your system is MacOS")
        # I beleivce it is same structure as Linux
    else:
        print("Unidentified system")

    #from panda3d.core import loadPrcFile
    #if __debug__:
    #    loadPrcFile("config.prc")

#----------------MAIN------------------/
class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        global mainMenuState
        global cameraActive
        # The background color
        base.setBackgroundColor(0,0,0)

        # THE MAIN MENU
        print('menuDEB1', mainMenuState)
        menu = S01_HOME.HOME.mainMenu(mainMenuState, cameraActive)
        print('menuDEB2', mainMenuState)

        # KEYBOARD INPUT
        self.accept('escape', self.quit)
        self.accept('m', self.menuToggle)
        #self.accept('arrow_down-repeat', self.moveCam)

    def menuToggle(self):
        S01_HOME.HOME.mainMenu(mainMenuState, cameraActive)

    def quit(self):
    	print("quitting shenko")
    	sys.exit()

# For making modules"
if __name__ == '__main__':
    print('main.py is being run directly')
    setupSequence()
    app = MyApp()
    app.run()
else:
    print("Shenko main is being imported, with no setup")
    app = MyApp()
    app.run()
