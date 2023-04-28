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
    global TITLE_FONT, BUTTON_FONT, OPTIONS_BUTTON_FONT
    global is_sound_on, difficulty

    #music
    pygame.mixer.init()
    #background_music = pygame.mixer.music.load('assets/Asteroid-Defense-Background.mp3')
    #pygame.mixer.music.play(-1)
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/Asteroid-Defense-Background.mp3'), -1)

    #create display
    SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 840
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroid Defense")
    BACKGROUND_COLOR = (31, 16, 43)
    ARCADE_FONT = pygame.font.Font("assets/ARCADE_N.TTF", 25)
    #using font in the fonts folder
    TITLE_FONT = pygame.font.Font("assets/ARCADE_N.TTF", 70)
    BUTTON_FONT = pygame.font.Font("assets/ARCADE_N.TTF", 50)
    OPTIONS_BUTTON_FONT = pygame.font.Font("assets/ARCADE_N.TTF", 30)
    #options
    is_sound_on = True
    difficulty = 'easy'


#menu screen
def main_menu():
    #display background color
    SCREEN.fill(BACKGROUND_COLOR)

    #get the mouse position
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    #display title text and center it
    title_text_1 = TITLE_FONT.render("ASTEROID", True, "Yellow")
    title_text_rect_1 = title_text_1.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8.5))
    title_text_2 = TITLE_FONT.render("DEFENSE", True, "Yellow")
    title_text_rect_2 = title_text_2.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/5))

    #display 3 buttons in the main menu, play, options, and quit
    #these three buttons are created via the button class provided in button.py
    PLAY_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.3), 
                        text_input="PLAY", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
    DIFFICULTY_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.96), 
                        text_input="DIFFICULTY", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.7), 
                        text_input="OPTIONS", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.5), 
                        text_input="QUIT", font=BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

    SCREEN.blit(title_text_1, title_text_rect_1)
    SCREEN.blit(title_text_2, title_text_rect_2)

    #cycle through every button and run the two functions
    #check to see if mouse is hovering over the button to change color
    #update it to the screen
    for button in [PLAY_BUTTON, DIFFICULTY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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
            elif DIFFICULTY_BUTTON.checkForInput(MENU_MOUSE_POS):
                #go to options screen
                controller.game_state = 'difficulty'
            elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                #go to options screen
                controller.game_state = 'options'
            elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                quit()
            #if player quits then exit game
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()

def difficulty_screen():
    global difficulty

    SCREEN.fill(BACKGROUND_COLOR)

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    #define buttons
    if difficulty == 'easy':
        EASY_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.2), 
                    text_input="EASY", font=OPTIONS_BUTTON_FONT, base_color="Blue", hovering_color="Blue")
        MEDIUM_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 
                    text_input="MEDIUM", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
        HARD_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.8), 
                    text_input="HARD", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
    elif difficulty == 'medium':
        EASY_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.2), 
                    text_input="EASY", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
        MEDIUM_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 
                    text_input="MEDIUM", font=OPTIONS_BUTTON_FONT, base_color="Blue", hovering_color="Blue")
        HARD_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.8), 
                    text_input="HARD", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
    else:
        EASY_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.2), 
                    text_input="EASY", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
        MEDIUM_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 
                    text_input="MEDIUM", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
        HARD_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.8), 
                    text_input="HARD", font=OPTIONS_BUTTON_FONT, base_color="Blue", hovering_color="Blue")

    BACK_BUTTON = Button(image=None, pos=(80, 30), 
                    text_input="BACK", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

    difficulty_text = TITLE_FONT.render("Difficulty", True, "White")
    difficulty_text_rect = difficulty_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8.5))

    for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, BACK_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                difficulty = 'easy'
            elif BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                controller.game_state = 'main_menu'
            elif MEDIUM_BUTTON.checkForInput(MENU_MOUSE_POS):
                difficulty = 'medium'
            elif HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                difficulty = 'hard'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                controller.game_state = 'main_menu'

    SCREEN.blit(difficulty_text, difficulty_text_rect)

def menu_shut_down():
    SCREEN.fill((255,255,255))

def change_sound(is_sound_on):
    if is_sound_on:
        pygame.mixer.Channel(0).unpause()
    else:
        pygame.mixer.Channel(0).pause()

def in_menu_options():
    global is_sound_on

    SCREEN.fill(BACKGROUND_COLOR)

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    #define buttons
    if is_sound_on:
        SOUND_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5), 
                    text_input="TURN SOUND OFF", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
    else:
        SOUND_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5), 
                    text_input="TURN SOUND ON", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

    BACK_BUTTON = Button(image=None, pos=(80, 30), 
                    text_input="BACK", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

    options_text = TITLE_FONT.render("Options", True, "White")
    options_text_rect = options_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8.5))

    for button in [SOUND_BUTTON, BACK_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if SOUND_BUTTON.checkForInput(MENU_MOUSE_POS):
                is_sound_on = not is_sound_on
                change_sound(is_sound_on)
            elif BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                controller.game_state = 'main_menu'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                controller.game_state = 'main_menu'

    SCREEN.blit(options_text, options_text_rect)
    

    

def in_game_options():
    global is_sound_on
    options = True

    while options:

        SCREEN.fill(BACKGROUND_COLOR)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #define buttons
        if is_sound_on:
            SOUND_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5), 
                        text_input="TURN SOUND OFF", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
        else:
            SOUND_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5), 
                        text_input="TURN SOUND ON", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

        BACK_BUTTON = Button(image=None, pos=(80, 30), 
                        text_input="BACK", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

        options_text = TITLE_FONT.render("Options", True, "White")
        options_text_rect = options_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8.5))

        for button in [SOUND_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if SOUND_BUTTON.checkForInput(MENU_MOUSE_POS):
                    is_sound_on = not is_sound_on
                    change_sound(is_sound_on)
                elif BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    options == False

        SCREEN.blit(options_text, options_text_rect)
        pygame.display.update()

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
                    in_game_options()
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
    global is_sound_on, difficulty
    pygame.display.set_caption("Asteroid Defense")
    BACKGROUND_COLOR = (31, 16, 43)

    player = Space_Ship()
    playerBullets = []
    asteroids = []
    not_gameover = True
    count = 0
    score = 0
    lives = 3

    #determine highest scores in difficulty
    score_file = open("assets/highscores.txt")
    easy_read = score_file.readline().split(',')
    medium_read = score_file.readline().split(',')
    hard_read = score_file.readline().split(',')
    easy_scores = [int(easy_read[2]),int(easy_read[4]),int(easy_read[6]),int(easy_read[8]),int(easy_read[10])]
    medium_scores = [int(medium_read[2]),int(medium_read[4]),int(medium_read[6]),int(medium_read[8]),int(medium_read[10])]
    hard_scores = [int(hard_read[2]),int(hard_read[4]),int(hard_read[6]),int(hard_read[8]),int(hard_read[10])]

    #determine difficulty
    if difficulty == 'easy':
        difficulty_modifier = 50
    elif difficulty == 'medium':
        difficulty_modifier = 35
    else:
        difficulty_modifier = 20
    while not_gameover:

        if lives == 0:
            new_highscore = False
            not_gameover = False
            if difficulty == 'easy':
                for highscore in easy_scores:
                    if score > highscore:
                        enter_new_highscore(score)
                        new_highscore = True
                        break
            elif difficulty == 'medium':
                for highscore in medium_scores:
                    if score > highscore:
                        enter_new_highscore(score)
                        new_highscore = True
                        break
            else:
                for highscore in hard_scores:
                    if score > highscore:
                        enter_new_highscore(score)
                        new_highscore = True
                        break
            if not new_highscore:
                gameover_screen()
            stats_screen(score)

        #this influences the number of asteroids spawning
        count += 1
        if count % difficulty_modifier == 0:
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
                    #play laser-shot.wav
                    if is_sound_on:
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/laser-shot.wav'))
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

def gameover_screen():
    global is_sound_on
    if is_sound_on:
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('assets/game-over.mp3'))
    target_time = pygame.time.get_ticks() + 3000
    while pygame.time.get_ticks() < target_time:
        SCREEN.fill("Red")

        gameover_text = TITLE_FONT.render("GAMEOVER", True, "White")
        gameover_text_rect = gameover_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        SCREEN.blit(gameover_text, gameover_text_rect)
        pygame.display.update()


def stats_screen(score):
    score_file = open("assets/highscores.txt")
    easy_scores = score_file.readline()
    medium_scores = score_file.readline()
    hard_scores = score_file.readline()
    in_stats_screen = True
    while in_stats_screen:
        SCREEN.fill(BACKGROUND_COLOR)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #define buttons
        MENU_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2.3, SCREEN_HEIGHT/1.1), 
                        text_input="MENU", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/1.8, SCREEN_HEIGHT/1.1), 
                        text_input="QUIT", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

        gameover_text = TITLE_FONT.render("HIGH SCORES", True, "Yellow")
        gameover_text_rect = gameover_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8.5))

        easy_text = OPTIONS_BUTTON_FONT.render(easy_scores.split(',')[0], True, "Red")
        easy_text_rect = easy_text.get_rect(center=(SCREEN_WIDTH/8, SCREEN_HEIGHT/4))

        #ran = random.choice([1, 1, 1, 2, 2, 3])

        #display easy scores
        width_1 = 70
        width_2 = 220
        easy_txt = easy_scores.split(',')
        display_scores(easy_txt, width_1, width_2)

        medium_text = OPTIONS_BUTTON_FONT.render(medium_scores.split(',')[0], True, "Red")
        medium_text_rect = medium_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))

        #display medium scores
        width_1 = 520
        width_2 = 670
        med_txt = medium_scores.split(',')
        display_scores(med_txt, width_1, width_2)

        hard_text = OPTIONS_BUTTON_FONT.render(hard_scores.split(',')[0], True, "Red")
        hard_text_rect = hard_text.get_rect(center=(SCREEN_WIDTH/1.2, SCREEN_HEIGHT/4))

        #display hard scores
        width_1 = 930
        width_2 = 1080
        hard_txt = hard_scores.split(',')
        display_scores(hard_txt, width_1, width_2)

        for button in [MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    controller.game_state = "main_menu"
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/Asteroid-Defense-Background.mp3'), -1)
                    in_stats_screen = False
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    controller.game_state = "main_menu"
                    in_gameover_screen == False

        SCREEN.blit(gameover_text, gameover_text_rect)
        SCREEN.blit(easy_text, easy_text_rect)
        SCREEN.blit(medium_text, medium_text_rect)
        SCREEN.blit(hard_text, hard_text_rect)
        pygame.display.update()

def enter_new_highscore(score):
    global is_sound_on
    if is_sound_on:
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('assets/success.mp3'))
    entering = True
    user_input = '___'
    curr_input_index = 0
    while entering:
        SCREEN.fill(BACKGROUND_COLOR)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #define buttons
        CONTINUE_BUTTON = Button(image=None, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.1), 
                        text_input="CONTINUE", font=OPTIONS_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

        new_highscore_text = TITLE_FONT.render("NEW HIGH SCORE", True, "Yellow")
        new_highscore_text_rect = new_highscore_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8.5))
        highscore_text = BUTTON_FONT.render("YOUR HIGH SCORE:" + str(score), True, "White")
        highscore_text_rect = highscore_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/5))

        CONTINUE_BUTTON.changeColor(MENU_MOUSE_POS)
        CONTINUE_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if len(user_input) == 3 and ('_' not in user_input):
                        entering = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_BACKSPACE) and ('_' not in user_input):
                    user_input = user_input[0:-1]
                    user_input += '_'
                elif (curr_input_index < 3):
                    new = list(user_input)
                    new[curr_input_index] = event.unicode
                    user_input = ''.join(new)
                    curr_input_index += 1

        user_text = BUTTON_FONT.render(user_input, True, "Green")
        user_text_rect = user_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        SCREEN.blit(user_text, user_text_rect)
        SCREEN.blit(new_highscore_text, new_highscore_text_rect)
        SCREEN.blit(highscore_text, highscore_text_rect)
        pygame.display.update()

    change_highscores(user_input, score)

def display_scores(dif_txt, width_1, width_2):
    curr_height = 300
    i = 0
    color_list = [(255,0,255),(0,255,255),(0,0,255),(0,255,0),(255,255,255)]
    c_list_index = 0
    for txt in dif_txt:

        if i != 0 and i != 11:
            if i%2 == 0:
                score_text = OPTIONS_BUTTON_FONT.render(txt, True, color_list[c_list_index%5])
                score_text_rect = score_text.get_rect(center=(width_2, curr_height))
                curr_height = curr_height + 70
                c_list_index += 1
            else:
                score_text = OPTIONS_BUTTON_FONT.render(txt, True, color_list[c_list_index%5])
                score_text_rect = score_text.get_rect(center=(width_1, curr_height))


            SCREEN.blit(score_text, score_text_rect)

        i += 1

def change_highscores(user_input, score):
    score_file = open("assets/highscores.txt")
    easy_line = score_file.readline()
    medium_line = score_file.readline()
    hard_line = score_file.readline()
    easy_strings = easy_line.split(',')
    medium_strings = medium_line.split(',')
    hard_strings = hard_line.split(',')

    easy_scores = [int(easy_strings[2]),int(easy_strings[4]),int(easy_strings[6]),int(easy_strings[8]),int(easy_strings[10])]
    medium_scores = [int(medium_strings[2]),int(medium_strings[4]),int(medium_strings[6]),int(medium_strings[8]),int(medium_strings[10])]
    hard_scores = [int(hard_strings[2]),int(hard_strings[4]),int(hard_strings[6]),int(hard_strings[8]),int(hard_strings[10])]

    easy_names = [easy_strings[1],easy_strings[3],easy_strings[5],easy_strings[7],easy_strings[9]]
    medium_names = [medium_strings[1],medium_strings[3],medium_strings[5],medium_strings[7],medium_strings[9]]
    hard_names = [hard_strings[1],hard_strings[3],hard_strings[5],hard_strings[7],hard_strings[9]]

    score_file.close()

    score_index = 0
    if difficulty == 'easy':
        for curr_score in easy_scores:
            if score > curr_score:
                ele = easy_scores.pop()
                easy_scores.insert(score_index, score)
                ele = easy_names.pop()
                easy_names.insert(score_index, user_input)

                new_line = 'easy,'

                for i in range(5):
                    new_line += easy_names[i]
                    new_line += ','
                    new_line += str(easy_scores[i])
                    new_line += ','
                new_line += '\n'

                with open('assets/highscores.txt', 'w') as f:
                    f.write(new_line)
                    f.write(medium_line)
                    f.write(hard_line)
                break

            score_index += 1
    elif difficulty == 'medium':
        for curr_score in medium_scores:
            if score > curr_score:
                ele = medium_scores.pop()
                medium_scores.insert(score_index, score)
                ele = medium_names.pop()
                medium_names.insert(score_index, user_input)

                new_line = 'medium,'

                for i in range(5):
                    new_line += medium_names[i]
                    new_line += ','
                    new_line += str(medium_scores[i])
                    new_line += ','
                new_line += '\n'

                with open('assets/highscores.txt', 'w') as f:
                    f.write(easy_line)
                    f.write(new_line)
                    f.write(hard_line)
                break

            score_index += 1
    else:
        for curr_score in hard_scores:
            if score > curr_score:
                ele = hard_scores.pop()
                hard_scores.insert(score_index, score)
                ele = hard_names.pop()
                hard_names.insert(score_index, user_input)

                new_line = 'hard,'

                for i in range(5):
                    new_line += hard_names[i]
                    new_line += ','
                    new_line += str(hard_scores[i])
                    new_line += ','
                new_line += '\n'

                with open('assets/highscores.txt', 'w') as f:
                    f.write(easy_line)
                    f.write(medium_line)
                    f.write(new_line)
                break

            score_index += 1