from settings import *


class Jeu:

    animation_cooldown = 100

    def __init__(
        self,
        animation_steps=50,
        frame_width=100,
        frame_height=100
    ):
        self.last_update = pygame.time.get_ticks()
        self.animation_steps = animation_steps
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame = 0

    # def animation(self, *args, **kwargs):
