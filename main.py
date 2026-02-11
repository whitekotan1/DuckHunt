import pygame, sys


pygame.init()

BACKGROUND = (211, 25, 11)



WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def main():
    looping = True

    while looping:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               looping = False

               
       WINDOW.fill(BACKGROUND)
       pygame.display.update()
       
    
    pygame.quit()
    sys.exit()






main()