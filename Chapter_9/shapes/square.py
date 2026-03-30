# square.py

# Square class

import pygame
import random

# Set up the colors
RED: tuple[int] = (255, 0, 0)
GREEN: tuple[int] = (0, 255, 0)
BLUE: tuple[int] = (0, 0, 255)


class Square:

    def __init__(self, window: pygame.Surface, max_width: int, max_height: int):
        self.window: pygame.Surface = window

        self.width_and_height: int = random.randrange(10 ,100)
        self.color: tuple[int] = random.choice((RED, GREEN, BLUE))
        self.x: int = random.randrange(1, max_width - 100)
        self.y: int = random.randrange(25, max_height - 100)
        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, self.width_and_height, self.width_and_height)
        self.shape_type: str = "Square"

    def clicked_inside(self, mouse_point: tuple[int]) -> bool:
        clicked: bool = self.rect.collidepoint(mouse_point)

        return clicked

    def get_type(self) -> str:
        return self.shape_type

    def get_area(self) -> int:
        the_area: int = self.width_and_height * self.width_and_height

        return the_area

    def draw(self) -> None:
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width_and_height, self.width_and_height))
