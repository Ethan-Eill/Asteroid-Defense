import pygame
import model
import view

#initiate game
def init():
    view.init()

#main game loop that controls all the input whilst playing the game
def game_loop():
    while True:
        #get events and loop through events
        events = pygame.event.get()
        for event in events:
            #if player quits then exit game
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
