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
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption("Système Solaire")

surface = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

## Fonction pour calculer la position d'une planète sur son orbite

# def calculate_orbit_position(angle, orbit_radius):
#     x = SCREEN_WIDTH // 2 + orbit_radius * math.cos(math.radians(angle))
#     y = SCREEN_HEIGHT // 2 + orbit_radius * math.sin(math.radians(angle))
#     return int(x), int(y)


# Boucle principale
clock = pygame.time.Clock()
angles = {planet: 0 for planet in ORBIT_RADIUS.keys()}
bg_img = pygame.image.load("../assets/background.jpg")
# background = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_rect = bg_img.get_rect(center=screen_rect.center)

running = True
zoom_factor = 1.0
font = pygame.font.Font(None, 24)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        zoom_factor += 0.01  # Increase zoom factor
        if zoom_factor > 2:
            zoom_factor = 2
    elif keys[pygame.K_e]:
        zoom_factor -= 0.01  # Decrease zoom factor, clamp it to be greater than 0
        if zoom_factor < 1:
            zoom_factor = 1


    # screen.blit(background, (0, 0))

    # # Dessiner le soleil
    # pygame.draw.circle(screen, YELLOW, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), SUN_RADIUS)
    #
    # # Dessiner les planètes et leurs orbites
    # for planet, radius in ORBIT_RADIUS.items():
    #     angle = angles[planet]
    #     planet_pos = calculate_orbit_position(angle, radius)
    #     pygame.draw.circle(screen, BLUE if planet != "Mars" else RED, planet_pos, PLANET_RADIUS)
    #     pygame.draw.circle(screen, RED, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), radius, 1)
    #     angles[planet] += 360 / ORBIT_PERIOD[planet]  # Ajuster la vitesse de rotation

    surface.fill(BLACK)
    surface.blit(bg_img, bg_rect)

    surface_mod = pygame.transform.rotozoom(surface, 0, zoom_factor)
    surface_mod_rect = surface_mod.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Render zoom factor as text
    zoom_text = font.render(f"Zoom : x{zoom_factor:.2f}", True, WHITE)
    zoom_text_rect = zoom_text.get_rect(bottomright=(SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10))

    screen.fill(BLACK)
    screen.blit(surface_mod, surface_mod_rect)
    screen.blit(zoom_text, zoom_text_rect)

    pygame.display.flip()
    clock.tick(60)
    zoom = False
    unzoom = False

pygame.quit()
sys.exit()
