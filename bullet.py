import pygame

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 5

    def update(self):
        self.life -= 1

    def is_dead(self):
        return self.life <= 0

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 5)