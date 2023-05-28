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
import platform     # used in 'setupSequence()'
import site         # used in '*_sitePackages()'

# Used for 'Loading...' text
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode

from direct.gui.DirectGui import *
from direct.gui.OnscreenImage import OnscreenImage  # To draw the logo
# For rolling over button sounds
from panda3d.core import AudioSound

def setupSequence():
    # I want to know where to download Shenko Models/Assets
    # It may be different on certain platforms
    plt = platform.system()
    if plt == "Windows":
        print("Your system is Windows")
        # create a users 'workspace' in C:\
    elif plt == "Linux":
        print("Your system is Linux")
        linux_sitePackages()
    elif plt == "Darwin":
        print("Your system is MacOS")
        # I beleivce it is same structure as Linux
    else:
        print("System Unidentified")

    # Find shenko manifest and update if needed
    #       print("Checking shenko manifest")
    #       print("manifest OK, nothing to download")
    #       print("Current Working Directory: ", os.getcwd())
    #       print(os.listdir("."))

    #from panda3d.core import loadPrcFile
    #if __debug__:
    #    loadPrcFile("config.prc")

def linux_sitePackages():
    # Get site packages directories
    site_packages = site.getsitepackages()
    siteUserLocations = site.getusersitepackages()

    # Directory to join
    shenkoAppDir = 'shenko'

    # If paths get found later(below), we'll want to add them to .profile
    def pythonPathProfileAdd(file_path, word):
        #bashExportPathCmd = 'export PYTHONPATH=$PYTHONPATH:' + str(file_path)
        #try:
        #    pathAdd = subprocess.run([bashExportPathCmd], shell=True, check=True)
        #    print(pathAdd.stdout)
        #    #os.system('export PYTHONPATH=/usr/local/bin/python3.4')
        #except:
        #    print('Something went wrong, could not add $path to ~/.bash_profile')
        #    print('You can try and run shenko directly from: ')
        #    print(os.path.join(path, file_path, word))

        # You could add the path via your pythonrc file, which defaults to ~/.pythonrc
        try:
            sys.path.append(file_path)
            print('Added: ', file_path, ' To Python $PATHS')
        except:
            print('Something went wrong, could not add $path to ~/.pythonrc')
            print('You can try and run shenko directly from: ')
            print(os.path.join(path, file_path, word))

    # Check GLOBAL site package locations
    for site_package in site_packages:
        shenkoPath = os.path.join(site_package, shenkoAppDir)
        exists = os.path.exists(shenkoPath)
        if exists == True:
            print(f"Path: {shenkoPath} - Exists: {exists}")
            # This function will try to add shenko.py path to .profile
            pythonPathProfileAdd(shenkoPath, 'shenko.py')

    # Check USER site package location
    shenkoPath = os.path.join(siteUserLocations, shenkoAppDir)
    exists = os.path.exists(shenkoPath)
    if exists == True:
        print(f"Path: {shenkoPath} - Exists: {exists}")
        pythonPathProfileAdd(shenkoPath, 'shenko.py')

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

