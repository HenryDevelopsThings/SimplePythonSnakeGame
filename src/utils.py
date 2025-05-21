import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import random

def get_grid_center_position() -> pygame.Vector2:
    return pygame.Vector2(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
def get_random_grid_position() -> pygame.Vector2:
    return pygame.Vector2(random.randrange(0, SCREEN_WIDTH, 10), random.randrange(0, SCREEN_HEIGHT, 10))