# rectangle.py

# Rectangle class
from __future__ import annotations
import pygame
import random


# Set up the colors
RED: tuple[int] = (255, 0, 0)
GREEN: tuple[int] = (0, 255, 0)
BLUE: tuple[int] = (0, 0, 255)


class Rectangle:

    def __init__(self, window: pygame.Surface):
        self.window: pygame.Surface = window
        self.width: int = random.choice((20, 30, 40))
        self.height: int = random.choice((20, 30, 40))
        self.color: tuple[int] = random.choice((RED, GREEN, BLUE))
        self.x: int = random.randrange(0, 400)
        self.y: int = random.randrange(0, 400)
        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.area: int = self.width * self.height

    def clicked_inside(self, mouse_point: tuple[int]) -> bool:
        clicked: bool = self.rect.collidepoint(mouse_point)

        return clicked

    # Magic method called when you compare two Rectangle objects with the == operator
    def __eq__(self, o_other_rectangle: "Rectangle") -> bool:
        if not isinstance(o_other_rectangle, Rectangle):
            raise TypeError("Second object is was not a Rectangle")

        if self.area == o_other_rectangle.area:
            return True

        else:
            return False

    # Magic method called when you compare two Rectangle objects with the < operator
    def __lt__(self, o_other_rectangle: Rectangle) -> bool:
        if not isinstance(o_other_rectangle, Rectangle):
            raise TypeError("Second object is was not a Rectangle")

        if self.area < o_other_rectangle.area:
            return True

        else:
            return False

    # Magic method called when you compare two Rectangle objects with the > operator
    def __gt__(self, o_other_rectangle: Rectangle) -> bool:
        if not isinstance(o_other_rectangle, Rectangle):
            raise TypeError("Second object is was not a Rectangle")

        if self.area > o_other_rectangle.area:
            return True

        else:
            return False

    def get_area(self) -> int:
        return self.area

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
