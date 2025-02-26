import pygame
from enum import Enum

#lets make a bunch of events
SWITCH_TO_MENU          = pygame.event.custom_type()
START_COUNTDOWN_TO_GAME = pygame.event.custom_type()
START_GAME              = pygame.event.custom_type()
END_GAME_PAUSE          = pygame.event.custom_type()
QUIT_GAME               = pygame.event.custom_type() # shut it down
QUIT_PLAY               = pygame.event.custom_type() # give up on play and return to menu
PLAY_CLIP1              = pygame.event.custom_type()
PLAY_CLIP2              = pygame.event.custom_type()

DROP_ESSAY              = pygame.event.custom_type()
DROP_MATH               = pygame.event.custom_type()
SHOOT_GPT               = pygame.event.custom_type()
SHOOT_PHOTO_MATH        = pygame.event.custom_type()
BOOM                    = pygame.event.custom_type()

#lets make sone states
class GameStates(Enum):
    SHOWING_MENU        = 1
    COUNTDOWN_TO_GAME   = 2
    PLAYING_GAME        = 3
    SHOW_SCORE          = 4    
    EXIT                = 5