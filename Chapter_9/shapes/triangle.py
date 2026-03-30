# triangle.py

# Triangle class

import pygame
import random


# Set up the colors
RED: tuple[int] = (255, 0, 0)
GREEN: tuple[int] = (0, 255, 0)
BLUE: tuple[int] = (0, 0, 255)


class Triangle:

    def __init__(self, window: pygame.Surface, max_width: int, max_height: int):
        self.window: pygame.Surface = window

        self.width: int = random.randrange(10 ,100)
        self.height: int = random.randrange(10, 100)

        self.triangle_slope: float = -1 * (self.height / self.width)
        self.color: tuple[int] = random.choice((RED, GREEN, BLUE))
        self.x: int = random.randrange(1, max_width - 100)
        self.y: int = random.randrange(25, max_height - 100)
        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.shape_type: str = "Triangle"

    def clicked_inside(self, mouse_point: tuple[int]) -> bool:
        in_rect: bool = self.rect.collidepoint(mouse_point)

        if not in_rect:
            return False

        # Do some math to see if the point is inside the triangle
        x_offset: int = mouse_point[0] - self.x
        y_offset: int = mouse_point[1] - self.y

        if x_offset == 0:
            return True

        # Calculate the slope (rise over run)
        point_slope_from_y_intercept: float = (y_offset - self.height) / x_offset

        if point_slope_from_y_intercept < self.triangle_slope:
            return True

        else:
            return False

    def get_type(self) -> str:
        return self.shape_type

    def get_area(self) -> float:
        the_area: float = .5 * self.width * self.height

        return the_area

    def draw(self) -> None:
        pygame.draw.polygon(self.window, self.color,
                            ((self.x, self.y + self.height),
                             (self.x, self.y), (self.x + self.width, self.y)))
