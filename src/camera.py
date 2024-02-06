from settings import *

def camera_move(keys, zoom_factor):
    if keys[pygame.K_a]:
        zoom_factor += 0.025 * zoom_factor  # Increase zoom factor
        if zoom_factor > 2:
            zoom_factor = 2
    elif keys[pygame.K_e]:
        zoom_factor -= 0.025 * zoom_factor  # Decrease zoom factor, clamp it to be greater than 0
        if zoom_factor <= 0.12:
            zoom_factor = 0.12
    return float(zoom_factor)
