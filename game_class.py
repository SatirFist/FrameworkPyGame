import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from spriteclasses import *
from events_states import *
from SweptCircle import *

class GameClass:
    window_surface = None
    ui_manager = None
    image_background = None
    Game_Container = None    
    BackMenu = None
    berg = None
    base = None
    app = None
    lastbullettime = 0
    bulletdelay = 0.5 # seconds

 
    def __init__(self, app): 
        self.app = app
        self.window_surface = self.app.window_surface
        self.ui_manager = self.app.manager
        self.image_background = BackgroundSpriteClass(self.window_surface, "./Graphics/wall.png")  
        self.Game_Container = pygame_gui.core.UIContainer(relative_rect=pygame.Rect((0,0),(800,600)), manager=self.ui_manager)
        self.BackMenu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 560), (60, 30)), container= self.Game_Container,text='Back', manager=self.ui_manager)
        self.countdown = CountdownSpriteClass(self.window_surface, 400, 250)   
        self.lastbullettime = app.time_cumulative
        
        self.berg = ErikBergClass(self.window_surface)
        self.base = BaseStationClass(self.window_surface)
        #self.sound1_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((380, 180), (80, 30)), container= self.Game_Container,text='Sound 1', manager=self.ui_manager)
        #self.sound2_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((380, 240), (80, 30)), container= self.Game_Container,text='Sound 2', manager=self.ui_manager)
     
        #self.ship = SpriteClassFloating(self.window_surface,"./Graphics/Bee1.png","./Graphics/Bee2.png","./Graphics/Bee3.png", 20, 100)

    def handle_event(self, event):
        if event.type == SWITCH_TO_MENU:
            self.Game_Container.hide()   
        elif event.type == START_COUNTDOWN_TO_GAME:                  
            self.Game_Container.show()  
            self.countdown_to_game = self.app.time_cumulative                
            pygame.time.set_timer(pygame.event.Event(START_GAME), 4000, 1)         
        elif event.type == START_GAME:
            self.Game_Container.show()           
        elif event.type == QUIT_PLAY: # give up            
            self.Game_Container.hide()            
        elif event.type == END_GAME_PAUSE:            
            self.Game_Container.show()
            pygame.time.set_timer(pygame.event.Event(SWITCH_TO_MENU), 4000, 1) 
        elif event.type == QUIT_GAME:            
            self.Game_Container.hide()        
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:  
            #only if we are playing game, not in countdown    
            if self.app.currentState == GameStates.PLAYING_GAME:      
                if event.ui_element == self.BackMenu:
                    pygame.event.post(pygame.event.Event(QUIT_PLAY))  
        elif event.type == pygame.KEYDOWN:               
            if self.app.currentState == GameStates.PLAYING_GAME: # only process keyboard input when game is 'running
                key = event.unicode                
        elif event.type == pygame.MOUSEBUTTONDOWN:
                # handle MOUSEBUTTONUP  
            if self.app.currentState == GameStates.PLAYING_GAME:  
                if self.app.time_cumulative - self.lastbullettime > self.bulletdelay:
                    self.lastbullettime = self.app.time_cumulative
                    pos = pygame.mouse.get_pos()
                    loc = [405, 520]
                    nvec = normalize2D(sub2d(pos, loc))
                    if event.button == 1:
                        pygame.event.post(pygame.event.Event(SHOOT_GPT, {'Loc': loc, 'NVec':nvec}))                         
                    elif event.button == 3: # right click
                        pygame.event.post(pygame.event.Event(SHOOT_PHOTO_MATH, {'Loc': loc, 'NVec':nvec}))                         

    def do_DrawMain(self):
        if self.app.currentState != GameStates.SHOWING_MENU:  
            self.image_background.draw() 
            if self.app.currentState == GameStates.PLAYING_GAME:
                self.berg.draw(self.app.time_delta)
                self.base.draw(self.app.time_delta)        
        if self.app.currentState == GameStates.COUNTDOWN_TO_GAME:
            pass
        elif self.app.currentState == GameStates.SHOW_SCORE:
            pass
            
    def do_DrawOverlay(self): # for on top of UI elements
        if self.app.currentState == GameStates.COUNTDOWN_TO_GAME:
            self.countdown.draw(self.app.time_cumulative - self.countdown_to_game)        