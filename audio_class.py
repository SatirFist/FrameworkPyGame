import pygame
from pygame import mixer
from events_states import *

class App_SoundsClass():
    MenuSong = None
    GameSong = None
    Clip1 = None
    Clip2 = None    

    def __init__(self):
        mixer.init()
                
        self.MenuSong = mixer.Sound("./Audio/Menu.wav")                    
        self.GameSong = mixer.Sound("./Audio/Game.wav")                
        self.Clip1 = mixer.Sound("./Audio/Right.wav")
        self.Clip2 = mixer.Sound("./Audio/Wrong.wav")

    def handle_event(self, event):
        if event.type == SWITCH_TO_MENU:
            self.GameSong.stop()            
            self.MenuSong.play()
        if event.type == START_COUNTDOWN_TO_GAME:
            self.MenuSong.stop()
            self.GameSong.play()                    
        if event.type == PLAY_CLIP1:
            self.Clip1.play()
        if event.type == PLAY_CLIP2:
            self.Clip2.play()