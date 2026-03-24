# ball.py

import pygame
import random


# Ball class
class Ball:

    def __init__(self, window: pygame.Surface, window_width: int, window_height: int):
        self.window:  pygame.Surface = window       # remember the window, so we can draw later
        self.window_width: int = window_width
        self.window_height: int = window_height

        self.image: pygame.Surface = pygame.image.load("images/ball.png")

        # A rect is made up of [x, y, width, height]
        ball_rect: pygame.Surface = self.image.get_rect()
        self.width: int = ball_rect.width
        self.height: int = ball_rect.height
        self.max_width: int = window_width - self.width
        self.max_height: int = window_height - self.height

        # Pick a random starting position
        self.x: int = random.randrange(0, self.max_width)
        self.y: int = random.randrange(0, self.max_height)

        # Choose a random speed between -4 and 4, but not zero, in both the x and y directions
        speeds_list: list[int] = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.x_speed: int = random.choice(speeds_list)
        self.y_speed: int = random.choice(speeds_list)

    def update(self):
        # Check for hitting a wall. If so, change that direction.
        if (self.x < 0) or (self.x >= self.max_width):
            self.x_speed  *= -1

        if (self.y < 0) or (self.y >= self.max_height):
            self.y_speed *= -1

        # Update the Ball's x and y, using the speed in two directions
        self.x += self.x_speed
        self.y += self.y_speed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
