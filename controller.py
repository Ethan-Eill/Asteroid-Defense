import pygame
import model
from view import main_menu_view

#initiate game
def init():
    global game_state
    game_state = 'main_menu'
    main_menu_view.init()

#main game loop that controls all the input whilst playing the game
def game_loop():
    #game state is used to track which part of the game to display
    #ie main menu, game, options
    while True:
        #if the user is in the main menu
        if game_state == 'main_menu':
            main_menu_view.main_menu()
        elif game_state == 'play':
            print("in play game_state")
        elif game_state == 'options':
            print("in options game_state")
        pygame.display.update()
