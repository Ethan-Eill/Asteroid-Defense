import pygame
import controller
import random
from button import Button
from model import Space_Ship, Asteroid, Bullet


#initial setup for game window and display
def init():
    #initiate pygame
    pygame.init()

    #define global variables
    global SCREEN_WIDTH, SCREEN_HEIGHT
    global SCREEN
    global BACKGROUND_COLOR
    global ARCADE_FONT
    global TITLE_FONT, BUTTON_FONT

    #create display
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroid Defense")
    BACKGROUND_COLOR = (31, 16, 43)
    ARCADE_FONT = pygame.font.Font("assets/ARCADE_N.TTF", 25)
    #using font in the fonts folder
    TITLE_FONT = pygame.font.Font("assets/ARCADE_N.TTF", 70)
    BUTTON_FONT = pygame.font.Font("assets/ARCADE_N.TTF", 50)


#menu screen
def main_menu():
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
    PLAY_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5), 
                        text_input="PLAY", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 
                        text_input="OPTIONS", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.67), 
                        text_input="QUIT", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

    SCREEN.blit(title_text_1, title_text_rect_1)
    SCREEN.blit(title_text_2, title_text_rect_2)

    #cycle through every button and run the two functions
    #check to see if mouse is hovering over the button to change color
    #update it to the screen
    for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                #play the game
                menu_shut_down()
                controller.game_state = 'play'
            if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                #go to options screen
                controller.game_state = 'options'
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                quit()
            #if player quits then exit game
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()

def menu_shut_down():
    SCREEN.fill((255,255,255))

#pause functionality while in game
def pause():

    paused = True

    while paused:

        SCREEN.fill(BACKGROUND_COLOR)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #define buttons
        CONTINUE_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5), 
                        text_input="CONTINUE", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 
                        text_input="OPTIONS", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.67), 
                        text_input="QUIT", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

        pause_text = TITLE_FONT.render("Paused", True, "White")
        pause_text_rect = pause_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8.5))

        for button in [CONTINUE_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    paused = False
                elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    paused = False
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused == False

        SCREEN.blit(pause_text, pause_text_rect)
        pygame.display.update()
    

#check if a new wave should begin
def check_new_wave(wave_number ,score):
    target_time = pygame.time.get_ticks() + 3000
    while pygame.time.get_ticks() < target_time:
        waveText = ARCADE_FONT.render('WAVE ' + str(wave_number), 1, (255,255,255))
        SCREEN.blit(waveText, ((SCREEN_WIDTH- waveText.get_width())/2, SCREEN_HEIGHT/2))


#function for game loop of the main game
def start_game():
    pygame.init()
    global SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroid Defense")
    BACKGROUND_COLOR = (31, 16, 43)

    player = Space_Ship()
    playerBullets = []
    asteroids = []
    count = 0
    score = 0
    lives = 3
    while True:

        count += 1
        if count % 50 == 0:
            ran = random.choice([1, 1, 1, 2, 2, 3])
            asteroids.append(Asteroid(ran))

        for b in playerBullets:
            b.move()
            if b.check_off_screen():
                playerBullets.pop(playerBullets.index(b))

        for a in asteroids:
            a.x += a.xvelocity
            a.y += a.yvelocity

            #player collision with asteroid
            #not 100% working
            if (a.x >= player.pos.x - player.width//2 and a.x <= player.pos.x + player.width//2) or (a.x + a.width <= player.pos.x + player.width//2 and a.x + a.width >= player.pos.x - player.width//2):
                if(a.y >= player.pos.y - player.height//2 and a.y <= player.pos.y + player.height//2) or (a.y + a.height >= player.pos.y - player.height//2 and a.y + a.height <= player.pos.y + player.height//2):
                    lives -= 1
                    asteroids.pop(asteroids.index(a))


            #bullet collision
            for b in playerBullets:
                if (b.x >= a.x and b.x <= a.x + a.width) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.width:
                    if (b.y >= a.y and b.y <= a.y + a.height) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.height:
                        if a.rank == 3:
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        elif a.rank == 2:
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        asteroids.pop(asteroids.index(a))
                        playerBullets.pop(playerBullets.index(b))
                        score += 10
                        break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    playerBullets.append(Bullet(player))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

        #this line throws error once game is exited
        mouse_x, mouse_y = pygame.mouse.get_pos()
        SCREEN.fill(BACKGROUND_COLOR)
        player.update_ship(mouse_x, mouse_y)
        scoreText = ARCADE_FONT.render('Lives: ' + str(lives) + '   Score: ' + str(score), 1, (255,255,255))
        SCREEN.blit(scoreText, (SCREEN_WIDTH- scoreText.get_width() - 25, 25))
        for b in playerBullets:
            b.draw()
        for a in asteroids:
            a.draw()
        pygame.display.flip()
