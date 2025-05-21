import pygame
from apple import Apple
from snake import Snake
from menus import *
from constants import *
from utils import *


class SnakeGame:
    def __init__(self):
        self._running = True
        self._display_surface = None
        self.game_state = None
        self.start_menu = None
        self.game_over_menu = None
        self._clock = None
        self.snake = None
        self.apple = None
        self._move_delay = 150
        self.last_move = 0
        
    def on_init(self):
        pygame.init()
        
        # Initalize window and game state
        self._display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.game_state = "start_menu"
        self.start_menu = StartMenu()
        self.game_over_menu = GameOverMenu()
        
        # Initialize the snake and apple start position
        snake_start_pos = get_grid_center_position()
        self.snake = Snake(snake_start_pos)
        
        apple_start_pos = get_random_grid_position()
        self.apple = Apple(apple_start_pos)
        
        # Initialize the games clock
        self._clock = pygame.time.Clock()

    def on_loop(self):
        """
        Defines the games logic.
        """
        if self.game_state == "game_menu":
            self._display_surface.fill(BACKGROUND_COLOR)
            current_time = pygame.time.get_ticks()
            # Only moves the snake if the move delay has been reached
            if current_time - self.last_move > self._move_delay:
                # Moves the snake and checks for a collision
                if self.snake.move() is False or self.snake.check_collision():
                    self.game_state = "game_over_menu"
                # Sets the last move to the current time for the move delay
                self.last_move = current_time
            # Checks snakes collision with the apple
            if self.snake.position == self.apple.position:
                self.snake.add_segment(self.apple.position)
                self.apple.set_position(get_random_grid_position())
            
    def end_game(self):
        """
        Allows the game to be shut down from other functions
        """
        self._running = False
    
    def set_game_state(self, state: str):
        """
        Sets the game state for swapping between menus
        Args:
            state (str): state should only be:
            1. start_menu
            2. game_menu
            3. game_over_menu
        """
        self.game_state = state
    
    def on_render(self):
        """
        Draws everything to the screen
        """
        # START MENU
        if self.game_state == "start_menu":
            self.start_menu.draw_start_menu(self._display_surface)
        
        # GAME MENU
        elif self.game_state == "game_menu":
            self.snake.draw(self._display_surface)
            self.apple.draw(self._display_surface)
        
        # GAME OVER MENU
        elif self.game_state == "game_over_menu":
            self.game_over_menu.draw_game_over_menu(self._display_surface, self.snake.score)
        
        # Update screen and maintain FPS
        pygame.display.flip()
        self._clock.tick(FPS)

    def on_event(self, event: pygame.event):
        """
        Event handler for keyboard inputs. E.g quitting, movement, starting, restarting and quitting

        Args:
            event (pygame.event): event object from pygame
        """
        # Handle quitting
        if event.type == pygame.QUIT:
            self._running = False
        
        # Handle Movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.snake.set_direction('UP')
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.snake.set_direction('DOWN')
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.snake.set_direction('LEFT')
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.snake.set_direction('RIGHT')
            
            # Handle start input on the Start Menu
            elif event.key == pygame.K_SPACE and self.game_state!="game_over_menu":
                self.game_state = "game_menu"
                
            # Handle restarting the snake and apple position
            elif event.key == pygame.K_r and self.game_state!="start_menu":
                snake_start_pos = get_grid_center_position()
                self.snake = Snake(snake_start_pos)
                apple_start_pos = get_random_grid_position()
                self.apple = Apple(apple_start_pos)
                self.game_state = "game_menu"
            # Handle quitting the game on the game over menu
            elif event.key == pygame.K_q and self.game_state=="game_over_menu":
                self.end_game()

    def on_cleanup(self):
        """
        Cleans up the game before quitting.
        """
        pygame.quit()
        
    def on_execute(self):
        """
        OOP pygame logic.
        """
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

if __name__ == "__main__":
    # STARTS GAME
    snake_game = SnakeGame()
    snake_game.on_execute()

# Pygame (n.d.). Pygame Front Page — pygame v2.0.0.dev15 documentation. [online] www.pygame.org. Available at: https://www.pygame.org/docs/.
# Wikidot.com. (2022). Tutorials Basic - PyGame Tutorials. [online] Available at: http://pygametutorials.wikidot.com/tutorials-basic.
# Winters, K. (2023). How to create a Start menu and a Game Over screen with PyGame. [online] tipsmake.com. Available at: https://tipsmake.com/how-to-create-a-start-menu-and-a-game-over-screen-with-pygame [Accessed 20 May 2025].