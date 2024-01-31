from settings import *
import pygame, math


def calculate_orbit_position(angle, orbit_radius):
    x = SCREEN_WIDTH // 2 + orbit_radius * math.cos(math.radians(angle))
    y = SCREEN_HEIGHT // 2 + orbit_radius * math.sin(math.radians(angle))
    return int(x), int(y)


angles = {planet: 0 for planet in planets_data.keys()}


def simulation(screen):
    pygame.draw.circle(screen, YELLOW, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 200)

    for planet, data in planets_data.items():
        angle = angles[planet]
        planet_pos = calculate_orbit_position(angle, data["orbit_radius"])
        pygame.draw.circle(screen, BLUE if planet != "Mars" else RED, planet_pos, data["size"] // 2000)
        pygame.draw.circle(screen, RED, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), data["orbit_radius"], 1)
        angles[planet] += 360 / data["orbit_period"]  # Ajuster la vitesse de rotation
    pass
