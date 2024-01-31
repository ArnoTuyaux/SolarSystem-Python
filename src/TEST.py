import sys
import pygame
import math

# Initialisation de Pygame
pygame.init()

# Paramètres
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SUN_RADIUS = 30
PLANET_RADIUS = 10

# Données orbitales pour les planètes (en millions de kilomètres)
# Source : https://nssdc.gsfc.nasa.gov/planetary/factsheet/
ORBIT_RADIUS = {
    "Mercury": 57.9,
    "Venus": 108.2,
    "Earth": 149.6,
    "Mars": 227.9,
    "Jupiter": 778.6,
    "Saturn": 1433.5,
    "Uranus": 2872.5,
    "Neptune": 4495.1
}

# Périodes orbitales pour les planètes (en jours)
ORBIT_PERIOD = {
    "Mercury": 87.97,
    "Venus": 224.70,
    "Earth": 365.25,
    "Mars": 686.98,
    "Jupiter": 4332.59,
    "Saturn": 10759.22,
    "Uranus": 30688.5,
    "Neptune": 60182.0
}

# Couleurs
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Système Solaire")

# Fonction pour calculer la position d'une planète sur son orbite
def calculate_orbit_position(angle, orbit_radius):
    x = SCREEN_WIDTH // 2 + orbit_radius * math.cos(math.radians(angle))
    y = SCREEN_HEIGHT // 2 + orbit_radius * math.sin(math.radians(angle))
    return int(x), int(y)


# Boucle principale
clock = pygame.time.Clock()
angles = {planet: 0 for planet in ORBIT_RADIUS.keys()}
bg_img = pygame.image.load("../pixel_galaxy.png")
background = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    # Dessiner le soleil
    pygame.draw.circle(screen, YELLOW, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), SUN_RADIUS)

    # Dessiner les planètes et leurs orbites
    for planet, radius in ORBIT_RADIUS.items():
        angle = angles[planet]
        planet_pos = calculate_orbit_position(angle, radius)
        pygame.draw.circle(screen, BLUE if planet != "Mars" else RED, planet_pos, PLANET_RADIUS)
        pygame.draw.circle(screen, RED, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), radius, 1)
        angles[planet] += 360 / ORBIT_PERIOD[planet]  # Ajuster la vitesse de rotation

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
