#!/usr/bin/env python
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
import sys
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)
 
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

        # My first key binding
        self.accept('escape', self.quit)
        self.accept('arrow_down', self.moveCamDown)

    def quit(self):
    	print("quitting shenko")
    	sys.exit()

    def moveCamDown(self):
        print("Camera Function Not enabled")

def central():
    print("central: OK")
    print("LAUNCHING APP SEE /CENTRAL.PY")
    #app = MyApp()
    #app.run()

# For making modules"
if __name__ == '__main__':
    central()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    pass

