import pygame
import math
import view
import random

#holds all methods and stats behind the spaceship
class Space_Ship:
    def __init__(self):
        self.x = 450
        self.y = 450
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.img = pygame.image.load('assets/Space_Ship_v3.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (70,70))
        self.speed = 7
        self.heading = 0
        self.dirvec = 0
        self.dy = 0
        self.dx = 0

    #move ship and keep ship inbounds
    def update_ship(self, mouse_x, mouse_y):
        #variables for calculating angle for spaceship to turn
        correction_angle = 90
        player_rect = self.img.get_rect(center=self.pos)
        self.dx, self.dy = mouse_x - player_rect.centerx, mouse_y - player_rect.centery
        angle = math.degrees(math.atan2(-self.dy, self.dx)) - correction_angle
        self.dirvec = pygame.math.Vector2(0, self.speed).rotate(angle+180)
        mouse_pos = pygame.math.Vector2(mouse_x, mouse_y)
        self.heading = mouse_pos - self.pos

        keys = pygame.key.get_pressed()

        #movement keys
        if keys[pygame.K_w]:
            self.pos += self.heading * 0.02
        elif keys[pygame.K_s]:
            self.pos -= self.heading * 0.02
        elif keys[pygame.K_d]:
            self.pos.x += self.speed
        elif keys[pygame.K_a]:
            self.pos.x -= self.speed

        #keep ship in bounds
        if self.pos.x > view.SCREEN_WIDTH:
            self.pos.x = view.SCREEN_WIDTH
        elif self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.y > view.SCREEN_HEIGHT:
            self.pos.y = view.SCREEN_HEIGHT
        elif self.pos.y < 0:
            self.pos.y = 0

        rot_image = pygame.transform.rotate(self.img, angle)
        rot_image_rect = rot_image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

        view.SCREEN.blit(rot_image, rot_image_rect.topleft)

class Bullet(object):
    def __init__(self, player):
        #may need to change, supposes to be a list of 2 points
        self.point = player.pos
        self.x, self.y = self.point
        self.w = 4
        self.h = 6
        self.c, self.s = player.dirvec
        self.c = -self.c
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y += self.yv

    def draw(self):
        pygame.draw.rect(view.SCREEN, (255,255,255), [self.x, self.y, self.w, self.h])

    def check_off_screen(self):
        if self.x < -10 or self.x > view.SCREEN_WIDTH or self.y > view.SCREEN_HEIGHT or self.y < -10:
            return True
        else:
            return False

#holds all methods and stats behind the asteroids
class Asteroid(object):
    def __init__(self, rank):
        # rank the asteroids based on size
        self.rank = rank
        if self.rank == 1:
            self.image = pygame.image.load('assets/asteroid50.png').convert_alpha()
        elif self.rank == 2:
            self.image = pygame.image.load('assets/asteroid100.png').convert_alpha()
        else:
            self.image = pygame.image.load('assets/asteroid150.png').convert_alpha()
        self.width = 50 * rank
        self.height = 50 * rank
        # get a random point in the screen
        self.randomPoint =  random.choice([(random.randrange(0, view.SCREEN_WIDTH-self.width), random.choice([-1*self.height - 5, view.SCREEN_HEIGHT + 5])), (random.choice([-1*self.width - 5, view.SCREEN_WIDTH + 5]), random.randrange(0, view.SCREEN_HEIGHT - self.height))])
        self.x, self.y = self.randomPoint
        # if statements to make sure asteroid go in correct direction
        if self.x < view.SCREEN_WIDTH//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < view.SCREEN_HEIGHT//2:
            self.ydir = 1
        else:
            self.ydir = -1
        # get the speed of the asteroid
        self.xvelocity = self.xdir * random.randrange(1,3)
        self.yvelocity = self.ydir * random.randrange(1,3)

    def draw(self):
        view.SCREEN.blit(self.image, (self.x, self.y))


