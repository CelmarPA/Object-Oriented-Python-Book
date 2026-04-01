# circle.py

# Circle class

from shape import *
import math


class Circle(Shape):

    def __init__(self, window: pygame.Surface, max_width: int, max_height: int):
        super().__init__(window, "Circle", max_width, max_height)

        self.radius: int = random.randrange(10, 50)
        self.center_x: int = self.x + self.radius
        self.center_y: int = self.y + self.radius
        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, self.radius ** 2, self.radius ** 2)

    def clicked_inside(self, mouse_point: tuple[int]) -> bool:
        the_distance: float = math.sqrt(((mouse_point[0] - self.center_x) ** 2) +
                                        ((mouse_point[1] - self.center_y) ** 2))

        if the_distance <= self.radius:
            return True

        else:
            return False

    def get_area(self) -> int | float:
        the_area: float = math.pi * (self.radius ** 2)

        return the_area

    def draw(self) -> None:
        pygame.draw.circle(self.window, self.color, (self.center_x, self.center_y), self.radius, 0)
