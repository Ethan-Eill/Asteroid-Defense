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
        self.speed = 4

    #move ship and keep ship inbounds
    def update_ship(self, mouse_x, mouse_y):
        #variables for calculating angle for spaceship to turn
        correction_angle = 90
        player_rect = self.img.get_rect(center=self.pos)
        dx, dy = mouse_x - player_rect.centerx, mouse_y - player_rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - correction_angle
        dirvec = pygame.math.Vector2(0, self.speed).rotate(angle+180)
        mouse_pos = pygame.math.Vector2(mouse_x, mouse_y)
        heading = mouse_pos - self.pos

        keys = pygame.key.get_pressed()

        #movement keys
        if keys[pygame.K_w]:
            self.pos += heading * 0.02
        elif keys[pygame.K_s]:
            self.pos -= heading * 0.02
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

#holds all methods and stats behind the asteroids
class Asteroid:
    def _init_(self, x, y, speed):
        self.img = pygame.image.load('assets/asteroid.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (70,70))
        self.x = x
        self.y = y
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.speed = speed

    def update_asteroid(self):
        self.y += self.speed

