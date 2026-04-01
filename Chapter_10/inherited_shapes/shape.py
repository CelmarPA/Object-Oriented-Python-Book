# shape.py

# Shape class
#
# To be used as a base class for other classes

import random
import pygame
from abc import ABC, abstractmethod


# Set up the colors
RED: tuple[int] = (255, 0, 0)
GREEN: tuple[int] = (0, 255, 0)
BLUE: tuple[int] = (0, 0, 255)


class Shape(ABC):    # This is an abstract class

    def __init__(self, window: pygame.Surface, shape_type: str, max_with: int, max_height: int):
        self.window: pygame.Surface = window
        self.shape_type: str = shape_type
        self.color: tuple[int] = random.choice((RED, GREEN, BLUE))
        self.x: int = random.randrange(1, max_with - 100)
        self.y: int = random.randrange(25, max_height - 100)

    def get_type(self) -> str:
        return self.shape_type

    @abstractmethod
    def clicked_inside(self, mouse_point: tuple[int]) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_area(self) -> int | float:
        raise NotImplementedError

    @abstractmethod
    def draw(self) -> None:
        raise NotImplementedError
