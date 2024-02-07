import pygame.image

from settings import *


class Sun:
    def __init__(self):
        self.size = 300
        self.sprite = pygame.image.load("../assets/sun.png")
        self.sprite_sheet = SpriteSheet(self.sprite)
        self.animation_list = []

    def draw(self, screen, zoom_factor):
        screen.blit(self.animation_list[jeu.frame], (0, 0))

    def animation(self, steps):
        for x in range(steps):
            self.animation_list.append(self.sprite_sheet.get_image(x, jeu.frame_width, jeu.frame_height, 1, BLACK))


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
        self.animation_list = []
        self.pos = []

    def calculate_position(self, zoom_factor):
        x = (FULL_SCREEN_WIDTH // 2 + (self.orbit_radius * zoom_factor + sun.size * zoom_factor)
             * math.cos(math.radians(self.angle)))
        y = (FULL_SCREEN_HEIGHT // 2 + (self.orbit_radius * zoom_factor + sun.size * zoom_factor)
             * math.sin(math.radians(self.angle)))
        return int(x), int(y)

    def draw(self, screen, zoom_factor):
        pass
        # planet_pos = self.calculate_position(zoom_factor)
        # pygame.draw.circle(screen, RED, (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2),
        #                    self.orbit_radius * zoom_factor + sun.size * zoom_factor, 1)
        # pygame.draw.circle(screen, self.color, planet_pos, self.size // 1500 * zoom_factor)
        # self.angle += 360 / self.orbit_period  # Ajuster la vitesse de rotation


def simulation(screen, clock, frame, last_update):
    pygame.font.init()  # Initialise la police
    font = pygame.font.Font(None, 24)  # Définie la police
    running = True
    zoom_factor = 0.50  # coefficient de zoom
    # sun.animation(jeu.animation_steps)

    planet_list = []
    for planet_name, planet_data in planets_data.items():
        planet = Planete(planet_name, planet_data["orbit_radius"], planet_data["orbit_period"],
                         planet_data["size"], planet_data["color"])
        planet_list.append(planet)

    while running:
        screen.fill(WHITE)  # Clear de l'écran
        keys = pygame.key.get_pressed()  # Récupère la touche pressée
        zoom_factor = camera_move(keys, zoom_factor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False

        for planet in planet_list:
            for x in range(jeu.animation_steps):
                planet.animation_list.append(planet.sprite_sheet.get_image(x, jeu.frame_width, jeu.frame_height, 1, BLACK))

        # Soleil
        # sun.sprite = pygame.transform.scale(sun.sprite, (sun.size * zoom_factor, sun.size * zoom_factor))
        # sun.draw(screen, frame)
        pygame.draw.circle(screen, YELLOW, (FULL_SCREEN_WIDTH // 2, FULL_SCREEN_HEIGHT // 2), sun.size * zoom_factor)
        for planet in planet_list:
            planet.pos = planet.calculate_position(zoom_factor)
            current_sprite = planet.sprite_sheet.get_image(frame, jeu.frame_width, jeu.frame_height, zoom_factor, BLACK)

            # Calculate the new position for centering the sprite after zooming
            sprite_width, sprite_height = current_sprite.get_size()
            blit_x = (planet.pos[0] - sprite_width) // 2
            blit_y = (planet.pos[1] - sprite_height) // 2

            # Display the current frame with adjusted blit position
            screen.blit(current_sprite, (blit_x, blit_y))
            planet.angle += 360 / planet.orbit_period  # Ajuster la vitesse de rotation

        # # Planetes
        # for planet in planet_list:
        #     planet.draw(screen, zoom_factor)

        # Update animation
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= jeu.animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(sun.animation_list):
                frame = 0

        # Afficher le niveau de zoom
        zoom_text = font.render(f"Zoom : x{zoom_factor:.2f}", True, BLACK)
        screen.blit(zoom_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

