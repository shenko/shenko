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
class Central():
    def __init__(self):
        print("Central: ok")


# For making modules"
if __name__ == '__main__':
    print('central node is being run directly')
    print('See: ../shenko/shenko.py to see how to import it!')
else:
    # print("main.py is being imported")
    pass
