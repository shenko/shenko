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

# Python imports
import os
import sys

# Panda imports
from pandac.PandaModules import WindowProperties
from direct.showbase.ShowBase import ShowBase

# Local imports
import s00_init

class shenkoApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # The background color
        base.setBackgroundColor(0,0,0)
        # Add a title to the window
        win_props = WindowProperties()
        win_props.setTitle('Shenko.org')
        self.win.requestProperties(win_props)

        self.rollSound = base.loader.loadSfx("assets/audio/click.ogg")


        state = s00_init.AppState("Application")
        state.request("Menu")

        # Input
        self.accept('escape', s00_init.quit)
        self.accept("f11", s00_init.toggle_fullscreen)
        #self.accept('m', self.menuToggle)
        #self.accept('arrow_down-repeat', self.moveCam)

# For making modules"
if __name__ == '__main__':
    print('main.py is being run directly')
    app = shenkoApp()
    app.run()
else:
    print("Shenko main is being imported, with no setup")
    app = shenkoApp()
    app.run()

