import pygame
from constants import *

class StartMenu:
    def __init__(self):
        # Initializes font
        self.font = load_font()
        
    def draw_start_menu(self, surface):
        """
        Draws a:
        1. Title
        2. Start "button"
        3. By Henry Dampier Text at the bottom right

        Args:
            surface (_type_): The surface at which the start menu is drawn to
        """
        # Renders the font
        title = self.font.render('Snake Game', True, (255, 255, 255))
        start_button = self.font.render('Press Space to start', True, (255, 255, 255))
        by_henry_dampier = self.font.render('- Henry Dampier', True, (255, 255, 255))
        # Draws the font to the screen
        surface.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, SCREEN_HEIGHT//2 - title.get_height()//2))
        surface.blit(start_button, (SCREEN_WIDTH//2 - start_button.get_width()//2, SCREEN_HEIGHT//2 + start_button.get_height()//2))
        # Padding for the bottom right text
        padding = 20
        surface.blit(by_henry_dampier, (SCREEN_WIDTH - by_henry_dampier.get_width() - padding, SCREEN_HEIGHT - by_henry_dampier.get_height() - padding))

class GameOverMenu:
    def __init__(self):
        # Initializes font
        self.font =  load_font()
        
    def draw_game_over_menu(self, surface, snake_segment_length: int):
        """
        Draws a:
        1. Game over text
        2. Score text
        3. Q TO QUIT text
        4. R To restart text

        Args:
            surface (_type_): the pygame surface to draw the text on
            snake_segment_length (int): the score/length of the snake
        """
        # Renders the font
        game_over_message = self.font.render('GAME OVER!', True, (255, 255, 255))
        score = self.font.render(f'Score: {snake_segment_length}', True, (255, 255, 255))
        q_to_quit = self.font.render('Q- Quit', True, (255, 255, 255))
        r_to_restart = self.font.render('R - Restart', True, (255, 255, 255))
        # Draws font to screen
        surface.blit(game_over_message, (SCREEN_WIDTH//2 - game_over_message.get_width()//2, SCREEN_HEIGHT//2 - game_over_message.get_height()//2))
        surface.blit(score, (SCREEN_WIDTH//2 - score.get_width()//2, SCREEN_HEIGHT//2 + score.get_height()//2))
        # Padding for the bottom right text
        padding = 20
        surface.blit(q_to_quit, (SCREEN_WIDTH - q_to_quit.get_width() - padding, SCREEN_HEIGHT - q_to_quit.get_height() - r_to_restart.get_height() - padding))
        surface.blit(r_to_restart, (SCREEN_WIDTH - r_to_restart.get_width() - padding, SCREEN_HEIGHT - r_to_restart.get_height() - padding))

def load_font(size=40) -> pygame.font:
    """
    Loads the pygame system arial font

    Args:
        size (int, optional): The size of the font. Defaults to 40.

    Returns:
        pygame.font: The system arial font at the arg size
    """
    return pygame.font.SysFont('arial', size)