from constants import *
import pygame

class Apple:
    def __init__(self, position: pygame.Vector2):
        """
        Initalizes the apples attributes

        Args:
            position (pygame.Vector2): Starting position of the apple
        """
        self.position = position
        self.size = SNAKE_SIZE
        self.color = APPLE_COLOR
        self.eaten = False
    def draw(self, surface: pygame.Surface):
        """
        Draws the apple to the screen

        Args:
            surface (pygame.Surface): Screen to draw the apple on
        """
        pygame.draw.rect(surface, self.color, (self.position.x, self.position.y, self.size, self.size))
    
    def set_position(self, new_position: pygame.Vector2):
        """
        Sets the apple to a new position

        Args:
            new_position (pygame.Vector2): Vector coordinates for the new apple
        """
        self.position = new_position