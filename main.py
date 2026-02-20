import pygame
import sys
from gun import Gun
from design import Design
from duck import Duck

pygame.init()
pygame.mixer.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Duck Hunt")

clock = pygame.time.Clock()

design = Design(WINDOW_WIDTH, WINDOW_HEIGHT)

gun = Gun()
duck = None
duck_spawned_once = False

DUCK_SPAWN_DELAY = 5000
last_duck_spawn_time = pygame.time.get_ticks()

start_sound = pygame.mixer.Sound("assets/sounds/start_game.wav")
start_sound.set_volume(0.8)

state = "menu"

font_big = pygame.font.SysFont(None, 36)
font_small = pygame.font.SysFont(None, 28)

button_rect = pygame.Rect(
    WINDOW_WIDTH // 2 - 50,
    WINDOW_HEIGHT // 2 + 20,
    100,
    40
)


def main():
    global state, duck, last_duck_spawn_time, duck_spawned_once

    running = True
    shots = 0
    hits = 0
    kills = 0

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if state == "menu" and button_rect.collidepoint(event.pos):
                    start_sound.play()
                    state = "game"
                    duck = None
                    duck_spawned_once = False
                    last_duck_spawn_time = pygame.time.get_ticks()

                elif state == "game":
                    if gun.ammo > 0:
                        gun.shoot(event.pos)
                        shots += 1

                        if duck and duck.alive and duck.is_hit(event.pos):
                            duck.dead()
                            hits += 1
                            kills += 1
                            duck = None
                            last_duck_spawn_time = pygame.time.get_ticks()



        design.draw(WINDOW)

        if state == "menu":
            text = font_big.render("Ready to start the game", True, (255, 255, 255))
            WINDOW.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, 120))

            pygame.draw.rect(WINDOW, (0, 200, 0), button_rect)
            go_text = font_small.render("GO", True, (0, 0, 0))
            WINDOW.blit(
                go_text,
                (
                    button_rect.centerx - go_text.get_width() // 2,
                    button_rect.centery - go_text.get_height() // 2
                )
            )

        elif state == "game":
            current_time = pygame.time.get_ticks()

            if duck is None:
                if current_time - last_duck_spawn_time >= DUCK_SPAWN_DELAY:
                    duck = Duck(WINDOW_WIDTH, WINDOW_HEIGHT)
                    duck_spawned_once = True
            else:
                if duck.alive:
                    duck.update()
                    duck.draw(WINDOW)

            gun.update()
            gun.draw(WINDOW)
            gun.draw_ammo(WINDOW)

            if gun.ammo == 0 and duck_spawned_once:
                state = "game_over"


        elif state == "game_over":

            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

            overlay.set_alpha(180)

            overlay.fill((0, 0, 0))

            WINDOW.blit(overlay, (0, 0))

            title = font_big.render("GAME OVER", True, (255, 80, 80))

            WINDOW.blit(

                title,

                (WINDOW_WIDTH // 2 - title.get_width() // 2, 90)

            )

            kills_text = font_small.render(

                f"Killed ducks: {kills}", True, (255, 255, 255)

            )

            WINDOW.blit(

                kills_text,

                (WINDOW_WIDTH // 2 - kills_text.get_width() // 2, 150)

            )

            accuracy = 0 if shots == 0 else int((hits / shots) * 100)

            acc_text = font_small.render(

                f"Accuracy: {accuracy}%", True, (255, 255, 255)

            )

            WINDOW.blit(

                acc_text,

                (WINDOW_WIDTH // 2 - acc_text.get_width() // 2, 180)

            )



        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


main()