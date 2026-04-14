# player.py

# Player

import pygame
from pygame import Surface
from pygwidgets import Image
from constants import *


class Player:

    def __init__(self, window: Surface) -> None:
        self.window: Surface = window
        self.image: Image = Image(self.window, (-100, -100), "images/player.png")

        player_rect: pygame.Rect = self.image.getRect()
        self.max_x: int = WINDOW_WIDTH - player_rect.width
        self.max_y: int = GAME_HEIGHT - player_rect.height

    # Every frame, move the Player icon to the mouse position
    # Limits the x- and y-coordinates to the game area of the window
    def update(self, x: int, y: int) -> pygame.Rect:
        if x < 0:
            x = 0

        elif x > self.max_x:
            x = self.max_x

        if y < 0:
            y = 0

        elif y > self.max_y:
            y = self.max_y

        self.image.setLoc((x, y))

        return self.image.getRect()

    def draw(self) -> None:
        self.image.draw()
