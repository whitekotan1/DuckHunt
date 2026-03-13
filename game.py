import pygame
import sys
import argparse
from design import Design
from gameManager import GameManager


class Game:
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Duck Hunt")

        self.clock = pygame.time.Clock()
        self.design = Design(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        self.start_sound = pygame.mixer.Sound("assets/sounds/start_game.wav")
        self.start_sound.set_volume(0.8)

        args = self._parse_args()
        self.selected_rounds = args.rounds

        self.state = "menu"
        self.gm = None
        self.running = False

        self.font_big = pygame.font.SysFont(None, 36)
        self.font_small = pygame.font.SysFont(None, 28)

        self.button_rect = pygame.Rect(self.WINDOW_WIDTH // 2 - 50, self.WINDOW_HEIGHT // 2 + 20, 100, 40)
        self.restart_rect = pygame.Rect(100, 230, 100, 40)
        self.quit_rect = pygame.Rect(210, 230, 100, 40)

    def _parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--rounds", type=int, default=1, help="Number of rounds (1-5)")
        return parser.parse_args()

    def _start_game(self):
        self.start_sound.play()
        self.state = "game"
        self.gm = GameManager(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.selected_rounds)

    def _restart_game(self):
        self.gm = GameManager(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.selected_rounds)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and self.state == "menu":
                if event.unicode.isdigit():
                    num = int(event.unicode)
                    if 1 <= num <= 5:
                        self.selected_rounds = num

            if event.type == pygame.KEYDOWN and self.state == "game" and self.gm and self.gm.state == "game_over":
                if event.key == pygame.K_r:
                    self._restart_game()
                if event.key == pygame.K_x:
                    self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.state == "menu" and self.button_rect.collidepoint(event.pos):
                    self._start_game()

                elif self.state == "game" and self.gm:
                    if self.gm.state == "game_over":
                        if self.restart_rect.collidepoint(event.pos):
                            self._restart_game()
                        elif self.quit_rect.collidepoint(event.pos):
                            self.running = False
                    else:
                        self.gm.handle_click(event.pos)

    def draw(self):
        self.design.draw(self.window)

        if self.state == "menu":
            text = self.font_big.render("Ready to start the game", True, (255, 255, 255))
            self.window.blit(text, (self.WINDOW_WIDTH // 2 - text.get_width() // 2, 120))

            pygame.draw.rect(self.window, (0, 200, 0), self.button_rect)
            go_text = self.font_small.render("GO", True, (0, 0, 0))
            self.window.blit(go_text, (
                self.button_rect.centerx - go_text.get_width() // 2,
                self.button_rect.centery - go_text.get_height() // 2
            ))

            round_text = self.font_small.render(
                f"Rounds: {self.selected_rounds} (press 1-5 on keyboard)", True, (255, 255, 255)
            )
            self.window.blit(round_text, (self.WINDOW_WIDTH // 2 - round_text.get_width() // 2, 170))

        elif self.state == "game" and self.gm:
            self.gm.draw(self.window)

    def update(self):
        if self.state == "game" and self.gm:
            self.gm.update()

    def run(self):
        self.running = True

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()