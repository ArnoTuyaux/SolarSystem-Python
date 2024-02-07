from settings import *


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
