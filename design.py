import pygame

class Design:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.image = pygame.image.load(
            "design/background.png"
        ).convert()

        self.image = pygame.transform.scale(
            self.image,
            (width, height)
        )

    def draw(self, screen):
        screen.blit(self.image, (0, 0))