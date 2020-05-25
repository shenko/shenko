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
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # My first key binding
        self.accept('escape', self.quit)
        self.accept('arrow_down-repeat', self.moveCam)

    def quit(self):
    	print("quitting shenko")
    	sys.exit()

    def moveCam(self):
        global camZ
        print("moving camera")
        camZ -= 5
        base.camera.setPos(camX, camY, camZ)

def central():
    print("central: OK")
    print("LAUNCHING APP SEE /CENTRAL.PY")
    app = MyApp()
    app.run()

# For making modules"
if __name__ == '__main__':
    central()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    pass

