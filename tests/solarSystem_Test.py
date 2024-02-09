import sys
from settings_test import *
from jeu_test import *


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()


# def focus_planet(screen, planets_data, planet_index, zoom_factor):
#     # Récupérer les données de la planète sélectionnée
#     selected_planet = list(planets_data.keys())[planet_index]
#     selected_data = planets_data[selected_planet]
#
#     # Calculer les nouvelles coordonnées du centre de l'écran en fonction de la position de la planète sélectionnée
#     new_center_x = FULL_SCREEN_WIDTH // 2 - selected_data["orbit_radius"] * zoom_factor
#     new_center_y = FULL_SCREEN_HEIGHT // 2
#
#     # Effacer l'écran
#     screen.fill((0, 0, 0))
#
#     # Dessiner l'orbite de la planète sélectionnée
#     pygame.draw.circle(screen, RED, (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2), selected_data["orbit_radius"] * zoom_factor, 1)
#
#     # Dessiner le système solaire en fonction des nouvelles coordonnées du centre de l'écran
#     for planet, data in planets_data.items():
#         # Calculer les nouvelles coordonnées de dessin en fonction de la position de la planète sélectionnée
#         relative_x = FULL_SCREEN_WIDTH // 2 - selected_data["orbit_radius"] * zoom_factor + data["orbit_radius"] * zoom_factor
#         planet_x = relative_x
#         planet_y = FULL_SCREEN_HEIGHT // 2
#         pygame.draw.circle(screen, data["color"], (planet_x, planet_y), data["size"] // 2 * zoom_factor)
#
#     # Dessiner un cercle autour de la planète sélectionnée pour la mettre en évidence
#     pygame.draw.circle(screen, (255, 255, 255), (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2), selected_data["orbit_radius"] * zoom_factor, 2)

#
#
#
#
#
# def calculate_orbit_position(angle, orbit_radius):
#     x = FULL_SCREEN_WIDTH // 2 + orbit_radius * math.cos(math.radians(angle))
#     y = FULL_SCREEN_HEIGHT // 2 + orbit_radius * math.sin(math.radians(angle))
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
#         if zoom_factor < 0.12:
#             zoom_factor = 0.12
#
#
# def simulation(screen, clock):
#     # Création de la fenêtre
#     screen = pygame.display.set_mode((FULL_SCREEN_WIDTH, FULL_SCREEN_HEIGHT))
#     screen_rect = screen.get_rect()
#     pygame.display.set_caption("Système Solaire")
#
#     surface = pygame.surface.Surface((FULL_SCREEN_WIDTH, FULL_SCREEN_HEIGHT))
#
#     clock = pygame.time.Clock()
#     clock.tick(50)
#
#     pygame.font.init()
#     font = pygame.font.Font(None, 24)
#     running = True
#     planet_index = 0
#     while running:
#         screen.fill(WHITE)
#         keys = pygame.key.get_pressed()
#         camera_move(keys)  # Gestion du zoom
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
#                 running = False
#             if keys[pygame.K_LEFT]:
#                 planet_index = (planet_index - 1) % len(planets_data)
#
#             if keys[pygame.K_RIGHT]:
#                 planet_index = (planet_index + 1) % len(planets_data)
#
#
#         # Dessiner le soleil
#         pygame.draw.circle(screen, YELLOW, (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2), 50 * zoom_factor)
#
#         # Draw a selection rectangle around the selected planet
#         selected_planet = list(planets_data.keys())[planet_index]
#         selected_data = planets_data[selected_planet]
#         selected_size = selected_data["size"] // 1500 * zoom_factor + 40  # Increase the size of the rectangle
#         selected_rect = pygame.Rect(0, 0, selected_size, selected_size)
#         selected_rect.center = calculate_orbit_position(angles[selected_planet],
#                                                         selected_data["orbit_radius"] * zoom_factor + 50 * zoom_factor)
#
#         pygame.draw.rect(screen, RED, selected_rect, 2)
#
#
#         for planet, data in planets_data.items():
#             angle = angles[planet]
#
#             # place planet on orbit + size of sun
#             planet_pos = calculate_orbit_position(angle, data["orbit_radius"] * zoom_factor + 50 * zoom_factor)
#             pygame.draw.circle(screen, RED, (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2),
#                                data["orbit_radius"] * zoom_factor + 50 * zoom_factor, 1)
#             pygame.draw.circle(screen, data["color"], planet_pos, data["size"] // 1500 * zoom_factor)
#
#             angles[planet] += 360 / data["orbit_period"]  # Ajuster la vitesse de rotation
#
#         # focus_planet(screen, planets_data, planet_index, zoom_factor)
#
#
#
#         # Afficher le niveau de zoom
#         zoom_text = font.render(f"Zoom : x{zoom_factor:.2f}", True, BLACK)
#         screen.blit(zoom_text, (10, 10))
#
#         select_text = font.render(f'Planet: {list(planets_data.keys())[planet_index]}', True, BLACK)
#         screen.blit(select_text, (10, 30))
#
#         pygame.display.flip()
#         clock.tick(60)
#
#     pygame.quit()
#     sys.exit()
#
#
# simulation(screen, clock)

import pygame.image
from math import *
# from settings import *
from camera import *

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale_factor, colour):
        original_image = pygame.Surface((width, height)).convert_alpha()
        original_image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        scaled_width = int(width * scale_factor)
        scaled_height = int(height * scale_factor)
        scaled_image = pygame.transform.scale(original_image, (scaled_width, scaled_height))
        scaled_image.set_colorkey(colour)
        return scaled_image


jeu_test = Jeu()


class Sun:
    def __init__(self):
        self.size = 300
        self.sprite = pygame.image.load("../assets/sun.png")
        self.sprite_sheet = SpriteSheet(self.sprite)
        self.animation_list = self.load_animation(jeu_test.animation_steps)

    def load_animation(self, steps):
        animation_list = []
        for x in range(steps):
            animation_list.append(self.sprite_sheet.get_image(x, jeu_test.frame_width, jeu_test.frame_height, 1, BLACK))
        return animation_list

    def draw(self, screen, frame):
        screen.blit(self.animation_list[frame], (0, 0))

sun = Sun()

class Planete:
    def __init__(self, name, orbit_radius, orbit_period, size, color):
        self.name = name
        self.orbit_radius = orbit_radius
        self.orbit_period = orbit_period
        self.size = size
        self.color = color
        self.angle = 0
        self.sprite_sheet_image = pygame.image.load('../assets/planets/Earth.png')
        self.sprite_sheet = SpriteSheet(self.sprite_sheet_image)
        self.animation_list = self.load_animation(jeu_test.animation_steps)
        self.pos = None

    def load_animation(self, steps):
        animation_list = []
        for x in range(steps):
            animation_list.append(self.sprite_sheet.get_image(x, jeu_test.frame_width, jeu_test.frame_height, 1, BLACK))
        return animation_list

    def calculate_position(self, zoom_factor, orbit_radius):
        # x = FULL_SCREEN_WIDTH // 2 + orbit_radius * math.cos(math.radians(angle))
        # #     y = FULL_SCREEN_HEIGHT // 2 + orbit_radius * math.sin(math.radians(angle))

        sun_radius = sun.size * zoom_factor  # Taille du soleil avec le facteur de zoom
        x = (FULL_SCREEN_WIDTH // 2 + orbit_radius * math.cos(math.radians(self.angle)))
        y = (FULL_SCREEN_HEIGHT // 2 + orbit_radius * math.sin(math.radians(self.angle)))
        return int(x), int(y)

    def draw(self, screen, zoom_factor):
        self.pos = self.calculate_position(zoom_factor, self.orbit_radius * zoom_factor + 50 * zoom_factor)
        current_frame = int(self.angle * len(self.animation_list) / 360)
        if current_frame >= len(self.animation_list):
            current_frame %= len(self.animation_list)  # Wrap around if current_frame exceeds list length
        current_sprite = self.animation_list[current_frame]

        # Calculate the new position for centering the sprite after zooming
        blit_x = self.pos[0] - (jeu_test.frame_width * zoom_factor) // 2
        blit_y = self.pos[1] - (jeu_test.frame_height * zoom_factor) // 2

        # Display the current frame with adjusted blit position
        screen.blit(current_sprite, (blit_x, blit_y))
        self.angle += 360 / self.orbit_period  # Adjust the rotation speed


last_update = pygame.time.get_ticks()
def simulation(screen, clock, frame, last_update):
    pygame.font.init()  # Initialise la police
    font = pygame.font.Font(None, 24)  # Définie la police
    running = True
    zoom_factor = 0.50  # coefficient de zoom
    sun.draw(screen, frame)  # Dessiner le soleil à l'initialisation du jeu_test
    planet_list = []
    for planet_name, planet_data in planets_data.items():
        planet = Planete(planet_name, planet_data["orbit_radius"], planet_data["orbit_period"],
                         planet_data["size"], planet_data["color"])
        planet_list.append(planet)
        planet.draw(screen, zoom_factor)  # Dessiner chaque planète à l'initialisation du jeu_test
    while running:
        screen.fill(WHITE)  # Clear de l'écran
        keys = pygame.key.get_pressed()  # Récupère la touche pressée
        zoom_factor = camera_move(keys, zoom_factor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False

        # Soleil
        # sun.sprite = pygame.transform.scale(sun.sprite, (sun.size * zoom_factor, sun.size * zoom_factor))
        # sun.draw(screen, frame)
        pygame.draw.circle(screen, YELLOW, (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2), sun.size * zoom_factor)
        for planet in planet_list:
            planet.draw(screen, zoom_factor)

        # Update animation
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= jeu_test.animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(sun.animation_list):
                frame = 0

        # Afficher le niveau de zoom
        zoom_text = font.render(f"Zoom : x{zoom_factor:.2f}", True, BLACK)
        screen.blit(zoom_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

simulation(screen, clock, jeu_test.frame, last_update)