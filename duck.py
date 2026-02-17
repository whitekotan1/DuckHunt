import pygame
import random

class Duck:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height

        self.x = random.randint(50, screen_width - 50)
        self.y = random.randint(50, screen_height - 50)

        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

        self.radius = 10 
        self.alive = True
        self.color = (81, 21, 65) 

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < self.radius or self.x > self.width - self.radius:
            self.speed_x = -self.speed_x
            
        if self.y < self.radius or self.y > self.height - self.radius:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)