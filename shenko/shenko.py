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

from direct.showbase.ShowBase import ShowBase

#-------------SYNOPSIS------------------/
"""
# Stepping manually didn't work for me
For an alternative, run() could not be called at all. Panda doesn’t really need
to own the main loop. Instead, taskMgr.step() can be called intermittently,
which will run through one iteration of Panda’s loop. In fact, run() is
basically just an infinite loop that calls Task.step() repeatedly.
taskMgr.step() must be called quickly enough after the previous call to
taskMgr.step(). This must be done quick enough to be faster than the frame rate.
This may useful when an imported third party python module that also has its own
event loop wants and wants to be in control of program flow. A third party
example may be Twisted, the event-driven networking framework.
"""
#--------------VARIABLES---------------/
#--------------FUNCTIONS---------------/
#----------------MAIN------------------/

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0,0,0)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        #self.scene = self.loader.loadModel("/media/shenko/shenko_HQ/0-TOC/shenko_website/website/public_html/public/library/civil/derp.gltf")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(1, 1, 1)    # 1:1 scale
        self.scene.setPos(0, 75, 0)     # X, Z, Y

        # Turns on/off wireframe mode
        self.scene.setRenderModeWireframe()

        # The shenko/S04_INPUTS folder holds everything
        # needed for Joystick / Mouse / Keyboards
        self.input_node = S04_INPUTS.Keyboard()

def main():
    print("main core is running!!!")
    S01_HOME.home()
    S02_FILESYSTEM.filesystem()
    S03_TEMPORARY.temporary()
    #S04_INPUTS.inputs()
    S05_CENTRAL.Central()
    S06_OUTPUT.output()
    S07_ROBOT_HOME.robotHome()
    S08_NETWORK.network()
    S09_EXTERNAL.external()

    # Run is just Task.step() looped
    app = MyApp()
    app.run()

# For making modules"
if __name__ == '__main__':
    main()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    print("shenko/shenko/shenko.py importing main")
    main()
