#!/usr/bin/env python
#FILE:          main.py
#SOURCE:        https://github.com/shenko/shenko/
#                blob/master/shenko/S05_CENTRAL/CENTRAL.py
__author__      = "Danny Dowshenko"
__copyright__   = "http://creativecommons.org/licenses/by/3.0/legalcode"
#DESCRIPTION:
"""
MAIN MENU that threads
    -each 'core' element is a thread
    -main listens to 'core'
"""
import os

def Central(mainMenuState):

    # Load the environment model.
    print("\n#------------Current Working Directory-----------/\n")
    pwd = os.getcwd()
    print(pwd)
    print("\n#------------Contents of Current Directory--------/\n")
    ls = os.listdir(".")
    print(ls)
    print("\n#-------------------------------------------------/\n")
    #self.scene = self.loader.loadModel("models/environment")
    #self.scene = self.loader.loadModel("/media/shenko/shenko_HQ/0-TOC/
    #...shenko_website/website/public_html/public/library/civil/derp.gltf")
    # Reparent the model to render.
    #self.scene.reparentTo(self.render)
    # Apply scale and position transforms on the model.
    #self.scene.setScale(1, 1, 1)    # 1:1 scale
    #self.scene.setPos(0, 75, 0)     # X, Z, Y

    # Turns on/off wireframe mode
    #self.scene.setRenderModeWireframe()
    #self.scene.setRenderModeFilled()

    # The shenko/S04_INPUTS folder holds everything
    # needed for Joystick / Mouse / Keyboards
    #self.input_node = S04_INPUTS.Keyboard(shareme)

    # How do I get back to main menu?
    print(mainMenuState)
    #self.accept('f', menuToggle)

def menuToggle():
    print("Starting to toggle")
    print("MENU STATE = ", mainMenuState)
    if mainMenuState == True:
        mainMenuState = False
        print("STATE CHANGE = ", mainMenuState)
    else:
        mainMenuState = True
        print("STATE CHANGE = ", mainMenuState)

# For making modules"
if __name__ == '__main__':
    print('central node is being run directly')
    print('See: ../shenko/shenko.py to see how to import it!')
else:
    # print("main.py is being imported")
    pass
