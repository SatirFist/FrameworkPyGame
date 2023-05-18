import pygame                           
from pygame_gui.core import ObjectID    
from spriteclasses import *             
from events_states import *
from app_class import *
from menu_class import *
from game_class import *
from audio_class import *
from bullets_n_bombs import *

app = AppClass()
menu = MenuClass(app)
game = GameClass(app)
audio = App_SoundsClass()
BnB = BnBClass(app)

app.currentState = GameStates.SHOWING_MENU
app.nextState = GameStates.SHOWING_MENU                    
pygame.event.post(pygame.event.Event(SWITCH_TO_MENU))  

while app.is_running:    
    app.updateClock()
    for event in pygame.event.get():                
        menu.handle_event(event)
        game.handle_event(event)
        audio.handle_event(event)
        BnB.handle_event(event)
        if event.type == SWITCH_TO_MENU:                            
            app.nextState = GameStates.SHOWING_MENU   
        elif event.type == START_COUNTDOWN_TO_GAME:                        
            app.nextState = GameStates.COUNTDOWN_TO_GAME            
        elif event.type == START_GAME:                        
            app.nextState = GameStates.PLAYING_GAME 
        elif event.type == QUIT_PLAY: # give up    
            pygame.event.post(pygame.event.Event(SWITCH_TO_MENU))                                  
        elif event.type == END_GAME_PAUSE:                        
            app.nextState = GameStates.SHOW_SCORE 
        elif event.type == QUIT_GAME:                        
            app.nextState = GameStates.EXIT                        
        elif event.type == pygame.QUIT:
            pygame.event.post(pygame.event.Event(QUIT_GAME))  
        app.manager.process_events(event)                

    app.manager.update(app.time_delta)
    menu.do_DrawMain()
    game.do_DrawMain()   
    BnB.do_DrawMain()     
    app.manager.draw_ui(app.window_surface)
    game.do_DrawOverlay()  
    menu.do_DrawOverlay()  
    pygame.display.update() 
    app.currentState = app.nextState # we had a state change, lets set it for next iteration of the look
    if app.currentState == GameStates.EXIT:
        app.is_running = False
pygame.quit()