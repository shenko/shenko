#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Shenko
===================

Shenko is a open source platform that uses the Panda3d game engine.
You can visit us on our website www.shenko.org
or find this code on github/shenko:
    https://github.com/shenko/shenko/blob/master/shenko/shenko.py

Author:
    Your Name <your@email.com>

License:
    The license information for your code.

"""

__author__      = "Shenko Development Team"
__email__       = "shenko.org@gmail.com"
__copyright__   = "http://creativecommons.org/licenses/by/3.0/legalcode"

# Standard library imports
import os
import sys

# Third-party imports
from direct.showbase.ShowBase import ShowBase

# Local imports


#--------------VARIABLES---------------/
mainMenuState = True
cameraActive = []     # if list is empty it is 'false'

#----------------MAIN------------------/
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        global mainMenuState

        # Debug
        print("escape key to exit, 'm' key to toggle menu")

        # The background color
        base.setBackgroundColor(0,0,0)

        # Main Menu
        if mainMenuState == True:
            print("Main Menu showing")
            # show mouse cursor

        # Input
        self.accept('escape', self.quit)
        self.accept('m', self.menuToggle)
        #self.accept('arrow_down-repeat', self.moveCam)

    def menuToggle(self):
        global mainMenuState
        if mainMenuState == True:
            mainMenuState = False
            #self.menuClass.hideMenu(mainMenuState)
            #del self.menuClass
            print("Main Menu is hidden")
        else:
            mainMenuState = True
            self.menuClass = mainMenu
            #menuChoice = str(self.menuClass)
            #print("CHA CHA CHOICES: ", menuChoice)
            print("Main Menu is showing")

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

