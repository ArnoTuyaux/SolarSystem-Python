from settings import *

angles = {planet: 0 for planet in planets_data.keys()}


def calculate_orbit_position(angle, orbit_radius):
    x = FULL_SCREEN_WIDTH // 2 + orbit_radius * math.cos(math.radians(angle))
    y = FULL_SCREEN_HEIGHT // 2 + orbit_radius * math.sin(math.radians(angle))
    return int(x), int(y)


def simulation(screen, clock):
    pygame.font.init()
    font = pygame.font.Font(None, 24)  # Initialise la police
    running = True
    zoom_factor = 1.0
    while running:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()
        zoom_factor = camera_move(keys, zoom_factor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False

        # Soleil
        pygame.draw.circle(screen, YELLOW, (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2), 35 * zoom_factor)

        # Planetes
        for planet, data in planets_data.items():
            angle = angles[planet]
            planet_pos = calculate_orbit_position(angle, data["orbit_radius"] * zoom_factor)
            pygame.draw.circle(screen,
                               BLUE if planet != "Mars" else RED,
                               planet_pos, data["size"] // 1500 * zoom_factor)
            pygame.draw.circle(screen,
                               RED,
                               (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2),
                               data["orbit_radius"] * zoom_factor, 1)
            angles[planet] += 360 / data["orbit_period"]  # Ajuster la vitesse de rotation

        # Afficher le niveau de zoom
        zoom_text = font.render(f"Zoom : x{zoom_factor:.2f}", True, BLACK)
        screen.blit(zoom_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)
