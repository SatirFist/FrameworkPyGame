import pygame
import math
import random
from events_states import *
from SweptCircle import *

class BombClass:
    surface = None
    window_surface = None
    loc = [] 
    nloc = [] 
    velocity = 0
    acceleration = 18
    speedcap = 100    
    isEssay = True
    deleteme = False

    def __init__(self, window_surface, isMath, x, y):
        self.loc = [x,y]
        self.nloc = [x,y]
        if isMath:
            self.isEssay = False
            self.surface =  pygame.image.load("./Graphics/math problem.png").convert_alpha()
        else:
            self.isEssay = True
            self.surface =  pygame.image.load("./Graphics/Essay.png").convert_alpha()
        self.window_surface = window_surface
    def calcnewpos(self, timedelta):
        self.velocity = self.velocity + self.acceleration * timedelta
        if self.velocity > self.speedcap:
            self.velocity = self.speedcap
        self.nloc = [self.loc[0], self.loc[1] + self.velocity * timedelta]        

    def draw(self, timedelta):
        self.loc = self.nloc        
        self.window_surface.blit(self.surface, self.nloc)   
        if self.loc[1] > 600:
            self.deleteme = True                 

class BulletClass:
    surface = None
    window_surface = None
    loc = []
    nvect = []
    velocity = 200
     
    isEssay = True
    deleteme = False

    def __init__(self, window_surface, isMath, loc, nvec):
        self.loc = loc
        self.nvect = nvec
        if isMath:
            self.isEssay = False
            self.surface =  pygame.image.load("./Graphics/PhotoMath.png").convert_alpha()
        else:
            self.isEssay = True
            self.surface =  pygame.image.load("./Graphics/ChatGPT.png").convert_alpha()
        self.window_surface = window_surface

    def calcnewpos(self, timedelta):
        oset = mult2dScaler(self.nvect, self.velocity * timedelta)        
        self.nloc = add2d(self.loc, oset)         

    def draw(self, timedelta):                        
       self.loc = self.nloc
       self.window_surface.blit(self.surface, self.loc)   
       if self.loc[0] < -16 or self.loc[0] > 800 or self.loc[1] < -16 or self.loc[1] > 600:
           self.deleteme = True      

class BnBClass:
    bombs = []
    bullets = []     
    app = None
    window_surface = None

    def __init__(self, app):
        self.app = app
        self.window_surface = app.window_surface

    def handle_event(self, event):
        if self.app.currentState == GameStates.PLAYING_GAME:            
            if event.type == DROP_ESSAY:                
                self.bombs.append(BombClass(self.window_surface, False, event.__dict__['X'], event.__dict__['Y']))
            if event.type == DROP_MATH:                
                self.bombs.append(BombClass(self.window_surface, True, event.__dict__['X'], event.__dict__['Y']))   
            if event.type == SHOOT_GPT:
                self.bullets.append(BulletClass(self.window_surface, False, event.__dict__['Loc'], event.__dict__['NVec']))                
            if event.type == SHOOT_PHOTO_MATH:
                self.bullets.append(BulletClass(self.window_surface, True, event.__dict__['Loc'], event.__dict__['NVec']))

    def do_DrawMain(self):                          
        if self.app.currentState == GameStates.PLAYING_GAME:
            for bomb in self.bombs:
                bomb.calcnewpos(self.app.time_delta)
            for bullet in self.bullets:
                bullet.calcnewpos(self.app.time_delta)
            # lets check for collisions
            for bomb in self.bombs:
                for bullet in self.bullets:
                    # if we collide, set to deleteme and send book event with location
                    #A is bomb and B is bullet
                    a1 = add2d(bomb.loc, [32,32])
                    a2 = add2d(bomb.nloc, [32,32])
                    b1 = add2d(bullet.loc, [16,16])
                    b2 = add2d(bullet.nloc, [16,16])                    
                    res = sphereoverlaps(32, a1, a2, 16, b1, b2)
                    if res[0] == True:                                               
                        bomb.deleteme = True
                        bullet.deleteme = True
                        pygame.event.post(pygame.event.Event(BOOM, {'Loc': bomb.loc}))
                    
                    

            for bomb in self.bombs:
                bomb.draw(self.app.time_delta)
            self.bombs = [elem for elem in self.bombs if elem.deleteme == False]  
            for bullet in self.bullets:
                bullet.draw(self.app.time_delta)
            self.bullets = [elem for elem in self.bullets if elem.deleteme == False]       