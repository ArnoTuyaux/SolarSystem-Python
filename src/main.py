import sys

import pygame
from settings import *


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moon Frontiers")
bg_img = pygame.image.load("../background.jpg")
background = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


def main():

    clock = pygame.time.Clock()
    pos_x = 0

    while True:

        clock.tick(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(background, (pos_x, 0))
        screen.blit(background, (SCREEN_WIDTH+pos_x, 0))

        if pos_x == -SCREEN_WIDTH:
            pos_x = 0

        pos_x -= 1

        pygame.display.update()


if __name__ == '__main__':
    main()
