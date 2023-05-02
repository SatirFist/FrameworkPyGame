import pygame
import math

class CountdownSpriteClass:
    surfacego = None
    surface1 = None
    surface2 = None
    surface3 = None
    location_x = 0
    location_y = 0   
    def __init__(self, window_surface,  start_x, start_y):
     
        self.surface1 =  pygame.image.load("./Graphics/Countdown1.png").convert_alpha()
        self.surface2 =  pygame.image.load("./Graphics/Countdown2.png").convert_alpha()
        self.surface3 =  pygame.image.load("./Graphics/Countdown3.png").convert_alpha()
        self.surfacego =  pygame.image.load("./Graphics/CountdownGo.png").convert_alpha()
        self.location_x = start_x
        self.location_y = start_y
        self.window_surface = window_surface
    def draw(self, delta_time):     
        amplitude_x = 5  # adjust this to change the width of the float
        amplitude_y = 10  # adjust this to change the height of the float
        frequency_x = 1  # adjust this to change the speed in the x direction
        frequency_y = 0.5  # adjust this to change the speed in the y direction
        x = amplitude_x * math.sin(2*math.pi*frequency_x*(delta_time))
        y = amplitude_y * math.cos(2*math.pi*frequency_y*(delta_time))
  
        if delta_time < 1.0:  
            rect = self.surface3.get_rect()          
            center_pos = rect.center
            self.window_surface.blit(self.surface3, (self.location_x + x - center_pos[0], self.location_y + y - center_pos[1]))
        elif delta_time < 2.0:
            rect = self.surface2.get_rect()          
            center_pos = rect.center
            self.window_surface.blit(self.surface2, (self.location_x + x - center_pos[0], self.location_y + y - center_pos[1]))
        elif delta_time < 3.0:
            rect = self.surface1.get_rect()          
            center_pos = rect.center
            self.window_surface.blit(self.surface1, (self.location_x + x - center_pos[0], self.location_y + y - center_pos[1]))
        else:
            rect = self.surfacego.get_rect()          
            center_pos = rect.center
            self.window_surface.blit(self.surfacego, (self.location_x + x - center_pos[0], self.location_y + y - center_pos[1]))  

class SpriteClassFloating:
    surface1 = None
    surface2 = None
    surface3 = None
    location_x = 0
    location_y = 0    
    movement_y = 40
    period_cycle_time = 5
    framerate_time = 2
    window_surface = None
    def __init__(self, window_surface, filename1, filename2, filename3, start_x, start_y):
        self.surface1 = pygame.image.load(filename1).convert_alpha()
        self.surface2 = pygame.image.load(filename2).convert_alpha()
        self.surface3 = pygame.image.load(filename3).convert_alpha()
        self.location_x = start_x
        self.location_y = start_y
        self.window_surface = window_surface

    def draw(self, cululative_time):
        frametime = cululative_time % self.framerate_time
        amplitude_x = 10  # adjust this to change the width of the float
        amplitude_y = 20  # adjust this to change the height of the float
        frequency_x = 1  # adjust this to change the speed in the x direction
        frequency_y = 0.5  # adjust this to change the speed in the y direction
        x = amplitude_x * math.sin(2*math.pi*frequency_x*(cululative_time))
        y = amplitude_y * math.cos(2*math.pi*frequency_y*(cululative_time))
        
        loc_y = self.location_y + y
        loc_x = self.location_x + x

        #every 1/3 of a second we want to change our 'frame' to a different picture
        if frametime < self.framerate_time * .90:
            self.window_surface.blit(self.surface1, (self.location_x, loc_y))
        elif frametime < self.framerate_time * .93:
            self.window_surface.blit(self.surface2, (self.location_x, loc_y))
        elif frametime < self.framerate_time * .96:
            self.window_surface.blit(self.surface3, (self.location_x, loc_y))
        else:
            self.window_surface.blit(self.surface2, (self.location_x, loc_y))    

class BackgroundSpriteClass:
    surface = None
    window_surface = None
    def __init__(self, window_surface, filename):
        self.window_surface = window_surface
        self.surface = pygame.image.load(filename).convert()

    def draw(self):
        self.window_surface.blit(self.surface, (0, 0))


class RobotSpriteClass:
    sprite = None
    location_x = 0
    location_y = 0   
    font1 = None
    textscore = None
    textWPM = None
    textErrors = None
    
    def __init__(self, window_surface, filename1,  start_x, start_y):
        self.sprite = pygame.image.load(filename1).convert_alpha()
        self.location_x = start_x
        self.location_y = start_y
        self.window_surface = window_surface     

    def draw(self, delta_time):     
        amplitude_x = 10  # adjust this to change the width of the float
        amplitude_y = 20  # adjust this to change the height of the float
        frequency_x = 1  # adjust this to change the speed in the x direction
        frequency_y = 0.5  # adjust this to change the speed in the y direction
        x = amplitude_x * math.sin(2*math.pi*frequency_x*(delta_time))
        y = amplitude_y * math.cos(2*math.pi*frequency_y*(delta_time))
        #pygame
        t_x = self.location_x + x
        t_y = self.location_y + y
        self.window_surface.blit(self.sprite, (t_x, t_y))
