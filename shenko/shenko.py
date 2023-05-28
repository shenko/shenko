#!/usr/bin/env python3
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

#import S01_HOME
#import S02_FILESYSTEM
#import S03_TEMPORARY
#import S04_INPUTS
#import S05_CENTRAL
#import S06_OUTPUT
#import S07_ROBOT_HOME
#import S08_NETWORK
#import S09_EXTERNAL

import S00_CORE.CORE
import S01_HOME.HOME
import S05_CENTRAL.CENTRAL

from direct.showbase.ShowBase import ShowBase

#-------------SYNOPSIS------------------/
"""
https://docs.panda3d.org/1.10/python/programming/tasks-and-events/tasks

# I think the only way to solve our dilema is to put a
# listner on CENTRAL
# and putter on every other node
"""
#--------------VARIABLES---------------/
mainMenuState = False
menuChoice = ''
cameraActive = []     # if list is empty it is 'false'

#----------------MAIN------------------/
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        global mainMenuState
        global menuChoice

        S00_CORE.CORE.setupSequence()

        # The background color
        base.setBackgroundColor(0,0,0)

        # Loading up the shenko core
        mainMenuState = S00_CORE.CORE.Core()    # menuToggle = True automatically when done

        # Creating a Menu Class
        self.menuClass = S00_CORE.CORE.mainMenu(mainMenuState)
        menuChoice = str(self.menuClass)
        print("CHA CHA CHOICES: ", menuChoice)

        # KEYBOARD INPUT
        self.accept('escape', self.quit)
        self.accept('m', self.menuToggle)
        #self.accept('arrow_down-repeat', self.moveCam)

    def menuToggle(self):
        global mainMenuState
        """
        mainMenuState = S00_CORE.CORE.menuToggle(mainMenuState)
        if mainMenuState != mainMenuState:
            mainMenuState = mainMenuState
        """
        if mainMenuState == True:
            mainMenuState = False
            self.menuClass.hideMenu(mainMenuState)
            del self.menuClass
        else:
            mainMenuState = True
            self.menuClass = S00_CORE.CORE.mainMenu(mainMenuState)
            menuChoice = str(self.menuClass)
            print("CHA CHA CHOICES: ", menuChoice)

    def quit(self):
    	print("quitting shenko")
    	sys.exit()

# For making modules"
if __name__ == '__main__':
    print('main.py is being run directly')
    app = MyApp()
    app.run()
else:
    print("Shenko main is being imported, with no setup")
    app = MyApp()
    app.run()

