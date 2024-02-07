import math
import sys

import pygame

from settings_test import *

#
#
# # Création de la fenêtre
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen_rect = screen.get_rect()
# pygame.display.set_caption("Système Solaire")
#
# surface = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
#
# clock = pygame.time.Clock()
# clock.tick(50)
#
#
# def calculate_orbit_position(angle, orbit_radius):
#     x = SCREEN_WIDTH // 2 + orbit_radius * math.cos(math.radians(angle))
#     y = SCREEN_HEIGHT // 2 + orbit_radius * math.sin(math.radians(angle))
#     return int(x), int(y)
#
#
# angles = {planet: 0 for planet in planets_data.keys()}
# zoom_factor = 1.0
#
#
# def camera_move(keys):
#     global zoom_factor
#     if keys[pygame.K_a]:
#         zoom_factor += 0.025 * zoom_factor  # Increase zoom factor
#         if zoom_factor > 2:
#             zoom_factor = 2
#     elif keys[pygame.K_e]:
#         zoom_factor -= 0.025 * zoom_factor  # Decrease zoom factor, clamp it to be greater than 0
#
#
# def simulation(screen, clock):
#     pygame.font.init()
#     font = pygame.font.Font(None, 24)
#     running = True
#     while running:
#         screen.fill(WHITE)
#         keys = pygame.key.get_pressed()
#         camera_move(keys)  # Gestion du zoom
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
#                 running = False
#
#         # Dessiner le soleil
#         pygame.draw.circle(screen, YELLOW, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 35 * zoom_factor)
#
#         # Dessiner les planètes et leurs orbites
#         for planet, data in planets_data.items():
#             angle = angles[planet]
#             planet_pos = calculate_orbit_position(angle, data["orbit_radius"] * zoom_factor)  # Appliquer le zoom à la position de la planète
#             pygame.draw.circle(screen, BLUE if planet != "Mars" else RED, planet_pos, data["size"] // 1500 * zoom_factor)
#             pygame.draw.circle(screen, RED, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), data["orbit_radius"] * zoom_factor, 1)  # Appliquer le zoom au rayon de l'orbite
#             angles[planet] += 360 / data["orbit_period"]  # Ajuster la vitesse de rotation
#
#         # Afficher le niveau de zoom
#         zoom_text = font.render(f"Zoom : x{zoom_factor:.2f}", True, BLACK)
#         screen.blit(zoom_text, (10, 10))
#
#         pygame.display.flip()
#         clock.tick(60)
#
#     pygame.quit()
#     sys.exit()
#
#
# simulation(screen, clock)


pygame.init()

screen = pygame.display.set_mode((FULL_SCREEN_WIDTH, FULL_SCREEN_HEIGHT))
running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)
current_planet = 0
sprite_sheet_image = pygame.image.load('../assets/27426372.png')
screen.fill(WHITE)

# class SpriteSheet:
#     def __init__(self, image):
#         self.sheet = image
#
#     def get_image(self, frame, width, height, scale, colour):
#         image = pygame.Surface((width, height)).convert_alpha()
#         image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
#         image = pygame.transform.scale(image, (width * scale, height * scale))
#         image.set_colorkey(colour)
#         return image





# Création des images individuelles à partir de la spritesheet
frames = []
frame_width = 200
frame_height = 200
for i in range(5):
    for j in range(10):
        frame = sprite_sheet_image.subsurface(i * frame_width, j * frame_height, frame_width, frame_height)
        frames.append(frame)


def test_index_select(screen, dico, key):
    return key


index = 0  # Indice pour sélectionner les images de la spritesheet
frame_counter = 0  # Counter to control animation speed

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill(WHITE)

    # Display the current frame
    screen.blit(frames[index], (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2))

    index = (index + 1) % len(frames)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
