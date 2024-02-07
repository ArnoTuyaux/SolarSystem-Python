import pygame, math
from camera import *
from animation import *
from jeu import *
jeu = Jeu()

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
    "Mercury": {"orbit_radius": 57.9, "orbit_period": 87.97, "size": 4879, "color": GREY},
    "Venus": {"orbit_radius": 108.2, "orbit_period": 224.70, "size": 12104, "color": ORANGE},
    "Earth": {"orbit_radius": 149.6, "orbit_period": 365.25, "size": 12756, "color": BLUE},
    "Mars": {"orbit_radius": 227.9, "orbit_period": 686.98, "size": 6792, "color": RED},
    "Jupiter": {"orbit_radius": 778.6, "orbit_period": 4332.59, "size": 142984, "color": YELLOW},
    "Saturn": {"orbit_radius": 1433.5, "orbit_period": 10759.22, "size": 120536, "color": GREY},
    "Uranus": {"orbit_radius": 2872.5, "orbit_period": 30688.5, "size": 51118, "color": CYAN},
    "Neptune": {"orbit_radius": 4495.1, "orbit_period": 60182.0, "size": 49528, "color": BLUE}
}

# Paramètres des planètes (nom, rayon, distance au Soleil, vitesse de rotation, couleur)

