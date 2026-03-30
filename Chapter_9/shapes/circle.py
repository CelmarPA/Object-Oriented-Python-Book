# circle.py

# Circle class

import pygame
import random
import math


# Set up the colors
RED: tuple[int] = (255, 0, 0)
GREEN: tuple[int] = (0, 255, 0)
BLUE: tuple[int] = (0, 0, 255)


class Circle:

    def __init__(self, window: pygame.Surface, max_width: int, max_height: int):
        self.window: pygame.Surface = window

        self.color: tuple[int] = random.choice((RED, GREEN, BLUE))
        self.x: int = random.randrange(1, max_width - 100)
        self.y: int = random.randrange(25, max_height - 100)
        self.radius: int = random.randrange(10, 50)
        self.center_x: int = self.x + self.radius
        self.center_y: int = self.y + self.radius
        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.shape_type: str = "Circle"

    def clicked_inside(self, mouse_point: tuple[int]) -> bool:
        distance: float = math.sqrt(((mouse_point[0] - self.center_x) ** 2) + ((mouse_point[1] - self.center_y) ** 2))

        if distance <= self.radius:
            return True

        else:
            return False

    def get_area(self) -> float:
        the_area: float = math.pi * (self.radius ** 2)

        return the_area

    def get_type(self) -> str:
        return self.shape_type

    def draw(self) -> None:
        pygame.draw.circle(self.window, self.color, (self.center_x, self.center_y), self.radius, 0)
