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
#import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText

from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *

# To draw the logo
from direct.gui.OnscreenImage import OnscreenImage

# For rolling over button sounds
from panda3d.core import AudioSound

from panda3d.core import TextNode

import sys
import os

def home(self):
    # Draws some text on the screen
    bk_text = "SHENKO"
    textObject = OnscreenText(text = bk_text, pos = (0.95,-0.95),
    scale = 0.05,fg=(0,1,1,1),bg=(0,0,0,.5),align=TextNode.ACenter,mayChange=1)

    rollSound = base.loader.loadSfx("click.ogg")

    # Callback function to set  text
    def startMN(self):
        bk_text = "LOADING..."
        textObject.setText(bk_text)

    # Callback function to set  text
    def mapMN(self):
        bk_text = "MAP MENU"
        textObject.setText(bk_text)

    # Callback function to set  text
    def optionsMN(self):
        bk_text = "OPTIONS MENU"
        textObject.setText(bk_text)

    # Callback function to set  text
    def helpMN(self):
        bk_text = "HELP MENU"
        textObject.setText(bk_text)

    # Callback function to set  text
    def exitMN(self):
        sys.exit()

    # Exit via button press in game or escape press by user
    #base.accept('escape', sys.exit)

    print os.getcwd()

    # Add button template
    imageObject = OnscreenImage(image ='logo.png', pos=(0, 0, .6), scale=0.5)
    imageObject.setImage('logo.png')
    #b = DirectButton(geom=loadImageAsPlane("logo.png"))
    #b = DirectButton(text = ("OK", "click!", "rolling over", "disabled"), scale=.05, command=setText)
    b = DirectButton(text = ("start", "---> start <---", "--> start <--", "disabled"), pos=(0,0,.2), scale=.07, rolloverSound=rollSound, command=startMN)
    b = DirectButton(text = ("map", "---> map <---", "--> map <--", "disabled"), pos=(0,0,.1), scale=.07, rolloverSound=rollSound, command=mapMN)
    b = DirectButton(text = ("options", "---> options <---", "--> options <--", "disabled"), pos=(0,0,0), rolloverSound=rollSound, scale=.07, command=optionsMN)
    b = DirectButton(text = ("help", "---> help <---", "--> help <--", "disabled"), pos=(0,0,-.1), scale=.07, rolloverSound=rollSound, command=helpMN)
    b = DirectButton(text = ("exit", "---> exit <---", "--> exit <--", "disabled"), pos=(0,0,-.2), scale=.07, rolloverSound=rollSound, command=exitMN)

# For making modules"
if __name__ == '__main__':
    home()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    pass
