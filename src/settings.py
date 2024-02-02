import pygame, math

# screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 780
FULL_SCREEN_WIDTH = 1920
FULL_SCREEN_HEIGHT = 1080

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (100, 100, 100)
ORANGE = (255, 0, 255)
CYAN = (0, 255, 255)


# Planet Info
planets_data = {
    "Mercury": {"orbit_radius": 57.9, "orbit_period": 87.97, "size": 4879},
    "Venus": {"orbit_radius": 108.2, "orbit_period": 224.70, "size": 12104},
    "Earth": {"orbit_radius": 149.6, "orbit_period": 365.25, "size": 12756},
    "Mars": {"orbit_radius": 227.9, "orbit_period": 686.98, "size": 6792},
    "Jupiter": {"orbit_radius": 778.6, "orbit_period": 4332.59, "size": 142984},
    "Saturn": {"orbit_radius": 1433.5, "orbit_period": 10759.22, "size": 120536},
    "Uranus": {"orbit_radius": 2872.5, "orbit_period": 30688.5, "size": 51118},
    "Neptune": {"orbit_radius": 4495.1, "orbit_period": 60182.0, "size": 49528}
}

# Paramètres des planètes (nom, rayon, distance au Soleil, vitesse de rotation, couleur)
planet_data = [
    ("Mercury", 0.05, 0.3871, 0.2056, math.radians(7), 0.2408, GREY),
    ("Venus", 0.1, 0.7233, 0.0067, math.radians(3.4), 0.6152, ORANGE),
    ("Earth", 0.1, 1.0, 0.0167, math.radians(0), 1.0, BLUE),
    ("Mars", 0.08, 1.5237, 0.0934, math.radians(1.9), 1.8809, RED),
    ("Jupiter", 0.3, 5.2028, 0.0484, math.radians(1.3), 11.862, ORANGE),
    ("Saturn", 0.25, 9.5388, 0.0542, math.radians(2.5), 29.457, YELLOW),
    ("Uranus", 0.2, 19.1914, 0.0472, math.radians(0.8), 84.02, CYAN),
    ("Neptune", 0.2, 30.0611, 0.0086, math.radians(1.8), 164.79, BLACK)
]
