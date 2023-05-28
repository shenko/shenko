#!/usr/bin/env python
#FILE:          main.py
#SOURCE:        https://github.com/shenko/shenko/
#                blob/master/shenko/S00_CORE/CORE.py
__author__      = "Danny Dowshenko"
__copyright__   = "http://creativecommons.org/licenses/by/3.0/legalcode"
#DESCRIPTION:
"""
MAIN MENU that threads
    -each 'core' element is a thread
    -main listens to 'core'
"""
import os
import sys
import time

# Used for 'Loading...' text
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode

from direct.gui.DirectGui import *
from direct.gui.OnscreenImage import OnscreenImage  # To draw the logo
# For rolling over button sounds
from panda3d.core import AudioSound

def Core():
    # SEE: Panda3d threading
    #   https://docs.panda3d.org/1.10/python/programming/tasks-and-events/threading
    print("Shenko Core Active")
    # Draws 'loading...' text on the screen while initializing
    bk_text = "Loading..."
    textObject = OnscreenText(text = bk_text, pos = (1.1,-.90),
    scale = 0.05,fg=(0,1,1,1),bg=(0,0,0,.5),align=TextNode.ACenter,mayChange=1)
    #textObject.setText(bk_text)

    # Needs Threading because this doesn't show 'loading...' text until the
    # whole app is finished being initialized
    #time.sleep(1)

    # we need to go to www.shenko.org, compare the manifest and update
    loading = True
    if loading == True:
        textObject.destroy()    # Done loading, remove 'loading...' text
        # in shenko.py SEE: S00_CORE.CORE.Core() in def __init__(self):
        return True

def menuToggle(mainMenuState):
    if mainMenuState == True:
        mainMenuState = False
        print("MENU STATE CHANGE = ", mainMenuState)
        return mainMenuState
    else:
        mainMenuState = True
        print("MENU STATE CHANGE = ", mainMenuState)
        return mainMenuState

class mainMenu:
    def __init__(self, mainMenuState):
        #self.mainMenuState = mainMenuState
        print("MenuClass Created: ", mainMenuState)
        self.imageObject = OnscreenImage(image ='logo.png', pos=(0, 0, .6), scale=0.5)
        #self.showMenu(mainMenuState)
        rollSound = base.loader.loadSfx("click.ogg")
        # Failed attempts include: command=self.sbuttonClicked, [...] / command=self.sbuttonClicked[...] / command=self.sbuttonClicked(...) is it a glitch???
        self.s = DirectButton(text = ("Single Player", "---> Single Player <---", "---> Single Player <---", "disabled"), pos=(0,0,.2), scale=.07, rolloverSound=rollSound, command=self.sbuttonClicked)
        self.m = DirectButton(text = ("Multi Player", "---> Multi Player <---", "---> Multi Player <---", "disabled"), pos=(0,0,.1), scale=.07, rolloverSound=rollSound, command=self.mbuttonClicked)
        self.o = DirectButton(text = ("Options", "---> Options <---", "---> Options <---", "disabled"), pos=(0,0,0), rolloverSound=rollSound, scale=.07, command=self.obuttonClicked)
        self.h = DirectButton(text = ("Help", "---> Help <---", "---> Help <---", "disabled"), pos=(0,0,-.1), scale=.07, rolloverSound=rollSound, command=self.hbuttonClicked)
        self.q = DirectButton(text = ("Quit", "---> Quit <---", "--> Quit <--", "disabled"), pos=(0,0,-.2), scale=.07, rolloverSound=rollSound, command=self.qbuttonClicked)

    def hideMenu(self, mainMenuState):
        print("debug=hide mainMenu", mainMenuState)
        self.imageObject.destroy()
        self.s.destroy()
        self.m.destroy()
        self.o.destroy()
        self.h.destroy()
        self.q.destroy()

    def sbuttonClicked(self):
        print('debug s')
        return 'singleplayer'

    def mbuttonClicked(self):
        print('debug m')
        return 'multiplayer'

    def obuttonClicked(self):
        print('debug o')
        return 'options'

    def hbuttonClicked(self):
        print('debug h')
        return 'help'

    def qbuttonClicked(self):
        print('debug q')
        #return 'quit'
        sys.exit()

# For making modules"
if __name__ == '__main__':
    print('core node is being run directly')
    print('See: ../shenko/shenko.py to see how to import it!')
else:
    # print("main.py is being imported")
    pass

