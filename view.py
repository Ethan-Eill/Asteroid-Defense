import pygame
from button import Button

#initial setup for game window and display
def init():
    #initiate pygame
    pygame.init()

    #define global variables
    global SCREEN_WIDTH, SCREEN_HEIGHT
    global SCREEN
    global BACKGROUND_COLOR
    global ARCADE_FONT

    #create display
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroid Defense")
    BACKGROUND_COLOR = (31, 16, 43)
    ARCADE_FONT = pygame.font.Font("assets/ARCADE_N.TTF", 25)


#menu screen
def main_menu():
    #using font in the fonts folder
    TITLE_FONT = pygame.font.Font("assets/ARCADE_N.TTF", 70)
    BUTTON_FONT = pygame.font.Font("assets/ARCADE_N.TTF", 50)

    #game loop while in the menu screen
    while True:
        #display background color
        SCREEN.fill(BACKGROUND_COLOR)

        #get the mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #display title text and center it
        title_text_1 = TITLE_FONT.render("ASTEROID", True, "Black")
        title_text_rect_1 = title_text_1.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8.5))
        title_text_2 = TITLE_FONT.render("DEFENSE", True, "Black")
        title_text_rect_2 = title_text_2.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/5.5))

        #display 3 buttons in the main menu, play, options, and quit
        #these three buttons are created via the button class provided in button.py
        PLAY_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3), 
                            text_input="PLAY", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5), 
                            text_input="OPTIONS", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, 470), 
                            text_input="QUIT", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(title_text_1, title_text_rect_1)
        SCREEN.blit(title_text_2, title_text_rect_2)

        #cycle through every button and run the two functions
        #check to see if mouse is hovering over the button to change color
        #update it to the screen
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        #main menu game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #play the game
                    print("Play")
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #go to options screen
                    print("Options")
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()