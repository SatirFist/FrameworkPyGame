import pygame                           
from pygame_gui.core import ObjectID    
from spriteclasses import *   

# this is to manage sprite displays.
# this class holds all the bitmap sprites (so they can be reused)
# it will also manage different levels of display 
# 100 will be the furthest back and all numbers lower will be on top of it
# 1 will be the last sprites to be drawn and thus be on the tippy top
# the GUI itself will be drawn as if it were 20 

class displayManagerClass():
    sprites = []   
    app = None 

    def __init__(self, app):
        self.app = app