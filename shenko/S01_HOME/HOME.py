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
#import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
# To draw the logo
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *
# For rolling over button sounds
from panda3d.core import AudioSound
from panda3d.core import TextNode
from panda3d.core import NodePath

import sys
import os

class mainMenu:
    def __init__(self, mainMenuState, cameraActive):
        # Just try and destroy a menu if it already exists
        try:
            self.hideMainMenu()
        except:
            # If nothing exists we create the main menu
            self.bk_text = "Welcome to SHENKO"
            self.textObject = OnscreenText(text = self.bk_text,
                                            pos = (0.95,-0.95),
                                            scale = 0.05,
                                            fg=(0,1,1,1),
                                            bg=(0,0,0,.5),
                                            align=TextNode.ACenter,
                                            mayChange=1)
            #  Draw the Shenko LOGO
            self.imageObject = OnscreenImage(image ='logo.png', pos=(0, 0, .6), scale=0.5)
            self.imageObject.setImage('logo.png')

            # Menu buttons
            rollSound = base.loader.loadSfx("click.ogg")
            self.startbttn = DirectButton(text = ("start", "---> start <---", "--> start <--", "disabled"),
                                            pos=(0,0,.2),
                                            scale=.07,
                                            rolloverSound=rollSound,
                                            command=self.start)
            self.mainMenuState = False
            print('derp', self.mainMenuState)

    def hideMainMenu(self):
        print("#---#### ####---#")
        #DirectButton.destroy()
        self.textObject.destroy()    # This is the text lower right of screen
        self.imageObject.destroy()   # This is the Logo
        self.startbttn['state'] = DGG.DISABLED
        self.startbttn.destroy()

    def start(self):
        print("LOADING CENTRAL --------------------------_> ...")
        self.hideMainMenu()

# For making modules"
if __name__ == '__main__':
    mainMenu()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    pass
