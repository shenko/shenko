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

from direct.gui.OnscreenText import OnscreenText

def home(self):

    textObject = OnscreenText(text = 'sub class working',
        pos = (-0.1, 0.09),
        scale = 0.07,
        fg = (0, 0, 255, 1))


# For making modules"
if __name__ == '__main__':
    home()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    pass
