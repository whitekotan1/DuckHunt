import pygame
from bullet import Bullet


class Gun:
    def __init__(self):
        self.max_ammo = 5
        self.ammo = self.max_ammo
        self.bullets = []

    def shoot(self, pos):
        if self.ammo <= 0:
            return

        self.ammo -= 1
        bullet = Bullet(pos[0], pos[1])
        self.bullets.append(bullet)

    def update(self):
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_dead():
                self.bullets.remove(bullet)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def draw_ammo(self, screen):
        start_x = screen.get_width() - 20 * self.max_ammo
        y = screen.get_height() - 25

        for i in range(self.max_ammo):
            if i < self.ammo:
                color = (255, 215, 0)   # патрон
            else:
                color = (100, 100, 100) # гільза

            pygame.draw.rect(
                screen,
                color,
                (start_x + i * 15, y, 10, 15)
            )