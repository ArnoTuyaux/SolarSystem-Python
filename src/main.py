import sys

from settings import *
from solarSystem import *
from jeu import Jeu


pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Moon Frontiers")
bg_img = pygame.image.load("../assets/Space_Background.png")
# background = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.transform.scale(bg_img, (FULL_SCREEN_WIDTH, FULL_SCREEN_HEIGHT))


def main():
    clock = pygame.time.Clock()
    pos_x = 0
    running = True

    while running:

        clock.tick(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    screen.fill(WHITE)
                    simulation(screen, clock, jeu.frame, jeu.last_update)
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.blit(background, (pos_x, 0))
        screen.blit(background, (FULL_SCREEN_WIDTH+pos_x, 0))

        if pos_x == -FULL_SCREEN_WIDTH:
            pos_x = 0

        pos_x -= 1

        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
