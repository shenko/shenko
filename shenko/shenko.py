#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Shenko
===================

Shenko is a open source platform that uses the Panda3d game engine.
You can visit us on our website www.shenko.org
or find this code on github/shenko:
    https://github.com/shenko/shenko/blob/master/shenko/shenko.py

Authors:
    SHENKO Development Team

License:
    # Copyright 2018 SHENKO
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

__author__      = "Shenko Development Team"
__email__       = "shenko.org@gmail.com"
__copyright__   = "http://creativecommons.org/licenses/by/3.0/legalcode"

# Standard library imports
import os
import sys

from s00_init import platformer, configurator

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

        # Access functions from platformer module
        platformer.start_platformer()
        platformer.jump()
        platformer.move("right")

        # Access functions from configurator module
        configurator.configure_settings()
        configurator.set_resolution(1920, 1080)
        configurator.set_volume(0.8)

        # Input
        self.accept('escape', self.quit)
        self.accept('m', self.menuToggle)
        #self.accept('arrow_down-repeat', self.moveCam)

    def menuToggle(self):
        global mainMenuState
        if mainMenuState == True:
            mainMenuState = False
            print("Main Menu is hidden")
        else:
            mainMenuState = True
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

