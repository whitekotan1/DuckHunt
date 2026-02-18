import pygame
import sys
from gun import Gun
from design import Design
from duck import Duck


pygame.init()


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BACKGROUND = (211, 25, 11)

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
design = Design(WINDOW_WIDTH, WINDOW_HEIGHT)
pygame.display.set_caption("Duck Hunt")

clock = pygame.time.Clock()


gun = Gun()
duck =Duck(WINDOW_WIDTH,WINDOW_HEIGHT)

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
    global state
    running = True

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # лкм


                    if state == "menu" and button_rect.collidepoint(event.pos):
                        state = "game"


                    elif state == "game":
                        gun.shoot(event.pos)

        design.draw(WINDOW)

        if state == "menu":

            text = font_big.render(
                "Ready to start the game",
                True,
                (255, 255, 255)
            )
            WINDOW.blit(
                text,
                (WINDOW_WIDTH // 2 - text.get_width() // 2, 120)
            )


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
            if duck.alive == True:
                duck.update()  
                duck.draw(WINDOW)  

            gun.update()
            gun.draw(WINDOW)
            gun.draw_ammo(WINDOW)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


main()