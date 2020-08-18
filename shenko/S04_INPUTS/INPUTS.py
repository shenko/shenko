#!/usr/bin/env python
#FILE:          main.py
#SOURCE:        viper/system/core/
__author__      = "Danny Dowshenko"
__copyright__   = "http://creativecommons.org/licenses/by/3.0/legalcode"
#DESCRIPTION:
import sys
from direct.showbase import DirectObject

"""
MAIN MENU that threads
    -each 'core' element is a thread
    -main listens to 'core'

ALLKEYS = [
  'left', 'right', 'up', 'down',
  'meta',
  'alt', 'lalt', 'ralt',
  'shift', 'lshift', 'rshift',
  'control', 'lcontrol', 'rcontrol',
  'shiftLock', 'scrollLock', 'capsLock', 'numLock',

  'space', 'enter', 'escape', 'backspace', 'tab',

  'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
  'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16',

  'del', 'insert', 'pause', 'printScreen', 'help',
  'home', 'end', 'pageDown', 'pageUp',

  'delete',

  '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
  ':', ';', '<', '=', '>', '?', '@',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
  '[', '\\', ']', '^', '_', '`',
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  '{', '|', '}', '~',
  '\n', '\t', '\r',
  '\x0c', '\x0b',
]
"""
class Keyboard(DirectObject.DirectObject):
    def __init__(self):
        self.accept('escape', self.quit)
        self.accept('mouse1', self.printHello)
        self.accept('arrow_down', self.moveCamDown)
        self.accept('arrow_up', self.up)

    def quit(self):
    	sys.exit()

    def printHello(self):
        print('Hello!')

    def up(self):
        print("UP Camera Function Not enabled")

    def moveCamDown(self):
        print("Camera Function Not enabled")

# For making modules"
if __name__ == '__main__':
    print('INPUTS.py is being run directly')
    print('See; ../shenko/shenko.py to see how to use it imported!')
else:
    #print("INPUTS.py is being imported")
    pass
