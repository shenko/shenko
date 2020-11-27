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
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0, 0, 0)

        # Load the environment model.
        print("\n#------------Current Working Directory-----------/\n")
        pwd = os.getcwd()
        print(pwd)
        print("\n#------------Contents of Current Directory--------/\n")
        ls = os.listdir(".")
        print(ls)
        print("\n#-------------------------------------------------/\n")
        self.scene = self.loader.loadModel("models/environment")
        #self.scene = self.loader.loadModel("/media/shenko/shenko_HQ/0-TOC/
        #...shenko_website/website/public_html/public/library/civil/derp.gltf")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(1, 1, 1)    # 1:1 scale
        self.scene.setPos(0, 75, 0)     # X, Z, Y

        # Turns on/off wireframe mode
        #self.scene.setRenderModeWireframe()
        #self.scene.setRenderModeFilled()

        # The shenko/S04_INPUTS folder holds everything
        # needed for Joystick / Mouse / Keyboards
        #self.input_node = S04_INPUTS.Keyboard(shareme)


# For making modules"
if __name__ == '__main__':
    print('central node is being run directly')
    print('See: ../shenko/shenko.py to see how to import it!')
else:
    # print("main.py is being imported")
    pass
