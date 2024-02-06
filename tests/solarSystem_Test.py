import sys
from settings_test import *


# Création de la fenêtre
screen = pygame.display.set_mode((FULL_SCREEN_WIDTH, FULL_SCREEN_HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption("Système Solaire")

surface = pygame.surface.Surface((FULL_SCREEN_WIDTH, FULL_SCREEN_HEIGHT))

clock = pygame.time.Clock()
clock.tick(50)


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






def calculate_orbit_position(angle, orbit_radius):
    x = FULL_SCREEN_WIDTH // 2 + orbit_radius * math.cos(math.radians(angle))
    y = FULL_SCREEN_HEIGHT // 2 + orbit_radius * math.sin(math.radians(angle))
    return int(x), int(y)


angles = {planet: 0 for planet in planets_data.keys()}
zoom_factor = 1.0


def camera_move(keys):
    global zoom_factor
    if keys[pygame.K_a]:
        zoom_factor += 0.025 * zoom_factor  # Increase zoom factor
        if zoom_factor > 2:
            zoom_factor = 2
    elif keys[pygame.K_e]:
        zoom_factor -= 0.025 * zoom_factor  # Decrease zoom factor, clamp it to be greater than 0
        if zoom_factor < 0.12:
            zoom_factor = 0.12


def simulation(screen, clock):
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    running = True
    planet_index = 0
    while running:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()
        camera_move(keys)  # Gestion du zoom

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
            if keys[pygame.K_LEFT]:
                planet_index = (planet_index - 1) % len(planets_data)

            if keys[pygame.K_RIGHT]:
                planet_index = (planet_index + 1) % len(planets_data)


        # Dessiner le soleil
        pygame.draw.circle(screen, YELLOW, (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2), 35 * zoom_factor)

        # Dessiner les planètes et leurs orbites
        for planet, data in planets_data.items():
            angle = angles[planet]
            planet_pos = calculate_orbit_position(angle, data["orbit_radius"] * zoom_factor)  # Appliquer le zoom à la position de la planète
            pygame.draw.circle(screen, data["color"], planet_pos, data["size"] // 1500 * zoom_factor)
            pygame.draw.circle(screen, RED, (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2), data["orbit_radius"] * zoom_factor, 1)  # Appliquer le zoom au rayon de l'orbite
            angles[planet] += 360 / data["orbit_period"]  # Ajuster la vitesse de rotation

        # focus_planet(screen, planets_data, planet_index, zoom_factor)

        # Dessiner un carré de sélection autour de la planète sélectionnée
        selected_planet = list(planets_data.keys())[planet_index]
        selected_data = planets_data[selected_planet]
        planet_pos = calculate_orbit_position(angles[selected_planet], selected_data["orbit_radius"] * zoom_factor)
        selected_size = selected_data["size"] // 1500 * zoom_factor + 20
        selected_rect = pygame.Rect(planet_pos[0] - selected_size // 2, planet_pos[1] - selected_size // 2,
                                    selected_size, selected_size)
        pygame.draw.rect(screen, RED, selected_rect, 2)

        # Afficher le niveau de zoom
        zoom_text = font.render(f"Zoom : x{zoom_factor:.2f}", True, BLACK)
        screen.blit(zoom_text, (10, 10))

        select_text = font.render(f'Planet: {list(planets_data.keys())[planet_index]}', True, BLACK)
        screen.blit(select_text, (10, 30))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


simulation(screen, clock)