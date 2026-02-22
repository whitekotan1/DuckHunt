import pygame
from gun import Gun
from duck import Duck


class GameManager:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.gun = Gun()
        self.duck = None
        self.duck_spawned_once = False

        self.DUCK_SPAWN_DELAY = 5000
        self.last_duck_spawn_time = pygame.time.get_ticks()

        self.shots = 0
        self.hits = 0
        self.kills = 0

        self.state = "playing"  

        self.font_big = pygame.font.SysFont(None, 36)
        self.font_small = pygame.font.SysFont(None, 28)

    def handle_click(self, pos):
        if self.gun.ammo > 0:
            self.gun.shoot(pos)
            self.shots += 1

            if self.duck and self.duck.alive and self.duck.is_hit(pos):
                self.duck.dead()
                self.hits += 1
                self.kills += 1
                self.duck = None
                self.last_duck_spawn_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()

        if self.duck is None:
            if current_time - self.last_duck_spawn_time >= self.DUCK_SPAWN_DELAY:
                self.duck = Duck(self.screen_width, self.screen_height)
                self.duck_spawned_once = True
        else:
            if self.duck.alive:
                self.duck.update()

        self.gun.update()

        if self.gun.ammo == 0 and self.duck_spawned_once:
            self.state = "game_over"

    def draw(self, screen):
        if self.state == "playing":
            if self.duck and self.duck.alive:
                self.duck.draw(screen)
            self.gun.draw(screen)
            self.gun.draw_ammo(screen)

        elif self.state == "game_over":
            overlay = pygame.Surface((self.screen_width, self.screen_height))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            title = self.font_big.render("GAME OVER", True, (255, 80, 80))
            screen.blit(title, (self.screen_width // 2 - title.get_width() // 2, 90))

            kills_text = self.font_small.render(f"Killed ducks: {self.kills}", True, (255, 255, 255))
            screen.blit(kills_text, (self.screen_width // 2 - kills_text.get_width() // 2, 150))

            accuracy = 0 if self.shots == 0 else int((self.hits / self.shots) * 100)
            acc_text = self.font_small.render(f"Accuracy: {accuracy}%", True, (255, 255, 255))
            screen.blit(acc_text, (self.screen_width // 2 - acc_text.get_width() // 2, 180))