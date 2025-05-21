import pygame
from constants import *

class Snake():
    def __init__(self, position: pygame.Vector2):
        """
        Initialize the snake properties

        Args:
            position (pygame.Vector2): starting position of the snake
        """
        self.direction = DEFAULT_DIRECTION
        self.position = position
        self.segment_list = [position]
        self.head = self.segment_list[0]
        self.score = 0
    
    def move(self) -> bool:
        """
        Handles the snake movement

        Returns:
            bool: returns if the snake is allowed to moves
        """
        # Stores previous x and y values for the next segment
        prev_x, prev_y = self.head.x, self.head.y
        # Changes the x and y position depending on the direction
        if self.direction == 'UP':
            self.head.y -= 10
        elif self.direction == 'DOWN':
            self.head.y += 10
        elif self.direction == 'LEFT':
            self.head.x -= 10
        elif self.direction == 'RIGHT':
            self.head.x += 10
        # Update each segment's position to follow the segment in front of it
        for segment in self.segment_list[1:]:
            segment.x, prev_x = prev_x, segment.x
            segment.y, prev_y = prev_y, segment.y

    def check_collision(self) -> bool:
        """
        Checks if there are any collisions with the screen edges or with the snake itself

        Returns:
            bool: returns if the snake has collided with anything
        """
        # Checks collision with screen
        if (self.head.x < 0 or self.head.x >= SCREEN_WIDTH or self.head.y < 0 or self.head.y >= SCREEN_HEIGHT):
            return True
        # Checks collision with itself
        for segment in self.segment_list[1:]:
            if self.head == segment:
                return True
        # Otherwise returns false as it does not collide
        return False   
         
    def draw(self, surface: pygame.Surface):
        """
        Draws the snake to the screen

        Args:
            surface (pygame.Surface): The display surface the snake is drawn to
        """
        for i in range(len(self.segment_list)):
            pygame.draw.rect(surface, SNAKE_COLOR, (self.segment_list[i].x, self.segment_list[i].y, SNAKE_SIZE, SNAKE_SIZE))
        
    def add_segment(self, position: pygame.Vector2):
        """
        Adds a segment to the snake vector array

        Args:
            position (pygame.Vector2): the position at which the segment is added
        """
        self.segment_list.append(position)
        # Sets the new score
        self.score = len(self.segment_list)-1
    
    def set_direction(self, new_direction: str):
        """
        Sets the direction of the snake to another direction. Ensures that the snake wont go back on itself

        Args:
            new_direction (str): The new direction of the snake. It can only be:
            1. UP
            2. DOWN
            3. LEFT
            4. RIGHT
        """
        opposites = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        # Ensures the new direction is not going back on itself
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction
