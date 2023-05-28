#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#FILE:          main.py
#SOURCE:        https://github.com/shenko/shenko/blob/master/shenko/shenko.py
__author__      = "Danny Dowshenko"
__copyright__   = "http://creativecommons.org/licenses/by/3.0/legalcode"
#DESCRIPTION:
"""
# MAIN MENU that threads
    -each 'core' element is a thread
    -main listens to 'core'

# To be tested:
After installing with pip, the path to my dirs seems to not registered
with the 'clients' $PATH so I get something like missing S01_HOME

To get the full path to the directory a Python file is contained in,
write this in that file:

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

"""
import sys
import os
import platform     # used in 'setupSequence()'
import site         # used in '*_sitePackages()'

#import S01_HOME
#import S02_FILESYSTEM
#import S03_TEMPORARY
#import S04_INPUTS
#import S05_CENTRAL
#import S06_OUTPUT
#import S07_ROBOT_HOME
#import S08_NETWORK
#import S09_EXTERNAL

#from S00_CORE.CORE import *
#import S00_CORE.CORE
#import S01_HOME.HOME
#import S05_CENTRAL.CENTRAL

from direct.showbase.ShowBase import ShowBase

#-------------SYNOPSIS------------------/
"""
https://docs.panda3d.org/1.10/python/programming/tasks-and-events/tasks

# I think the only way to solve our dilema is to put a
# listner on CENTRAL
# and putter on every other node
"""
#--------------VARIABLES---------------/
mainMenuState = False
menuChoice = ''
cameraActive = []     # if list is empty it is 'false'

#------------INIT FUNCTIONS-------------/
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


#----------------MAIN------------------/
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        global mainMenuState
        global menuChoice

        setupSequence()
        # With our path now added we can import shenko CORE
        # Then from there if Main is called we spin up the others
        # or if multi-player is called we do something else
        # or options etc...
        import S00_CORE

        # The background color
        base.setBackgroundColor(0,0,0)

        # Loading up the shenko core
        mainMenuState = S00_CORE.CORE.Core()    # menuToggle = True automatically when done

        # Creating a Menu Class
        self.menuClass = S00_CORE.CORE.mainMenu(mainMenuState)
        menuChoice = str(self.menuClass)
        print("CHA CHA CHOICES: ", menuChoice)

        # KEYBOARD INPUT
        self.accept('escape', self.quit)
        self.accept('m', self.menuToggle)
        #self.accept('arrow_down-repeat', self.moveCam)

    def menuToggle(self):
        global mainMenuState
        """
        mainMenuState = S00_CORE.CORE.menuToggle(mainMenuState)
        if mainMenuState != mainMenuState:
            mainMenuState = mainMenuState
        """
        if mainMenuState == True:
            mainMenuState = False
            self.menuClass.hideMenu(mainMenuState)
            del self.menuClass
        else:
            mainMenuState = True
            self.menuClass = S00_CORE.CORE.mainMenu(mainMenuState)
            menuChoice = str(self.menuClass)
            print("CHA CHA CHOICES: ", menuChoice)

    def quit(self):
    	print("quitting shenko")
    	sys.exit()

# For making modules"
if __name__ == '__main__':
    print('main.py is being run directly')
    app = MyApp()
    app.run()
else:
    print("Shenko main is being imported, with no setup")
    app = MyApp()
    app.run()

