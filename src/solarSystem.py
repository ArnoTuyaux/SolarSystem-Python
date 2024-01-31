import pygame

from settings import *


def calculate_orbit_position(angle, orbit_radius):
    x = SCREEN_WIDTH // 2 + orbit_radius * math.cos(math.radians(angle))
    y = SCREEN_HEIGHT // 2 + orbit_radius * math.sin(math.radians(angle))
    return int(x), int(y)


angles = {planet: 0 for planet in planets_data.keys()}


def camera_move(key):
    if key[pygame.K_s]:
        pass


def simulation(screen, clock):
    running = True
    while running:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False

        pygame.draw.circle(screen, YELLOW, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 35)

        for planet, data in planets_data.items():
            angle = angles[planet]
            planet_pos = calculate_orbit_position(angle, data["orbit_radius"])
            pygame.draw.circle(screen, BLUE if planet != "Mars" else RED, planet_pos, data["size"] // 1500)
            pygame.draw.circle(screen, RED, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), data["orbit_radius"], 1)
            angles[planet] += 360 / data["orbit_period"]  # Ajuster la vitesse de rotation


        pygame.display.flip()
        clock.tick(60)
