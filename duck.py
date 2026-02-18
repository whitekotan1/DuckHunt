import pygame
import random

class Duck:
    def __init__(self, screen_width, screen_height):

        self.width = screen_width
        self.height = screen_height

        self.x = random.randint(50, screen_width - 50)
        self.y = random.randint(50, screen_height - 50)

        self.speed_x = random.randint(-5, 5) or 1
        self.speed_y = random.randint(-5, 5) or 1

        self.img = pygame.image.load('design\duck-duckhunt.png')
        self.img = pygame.transform.scale(self.img, (50, 50))
        self.alive = True

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
        if self.x < 0 or self.x > self.width - 50:
            self.speed_x = -self.speed_x
        if self.y < 0 or self.y > self.height - 50:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        screen.blit(self.img, (int(self.x), int(self.y)))


    def dead(self):
         self.alive = False
         return self.alive


    