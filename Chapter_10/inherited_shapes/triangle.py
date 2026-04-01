# triangle.py

# Triangle class

from shape import *


class Triangle(Shape):

    def __init__(self, window: pygame.Surface, max_width: int, max_height: int):
        super().__init__(window, "Triangle", max_width, max_height)

        self.width: int = random.randrange(10, 100)
        self.height: int = random.randrange(10, 100)
        self.triangle_slop: float = -1 * (self.height / self.width)
        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clicked_inside(self, mouse_point: tuple[int]) -> bool:
        in_rect: bool = self.rect.collidepoint(mouse_point)

        if not in_rect:
            return False

        # Do some math to see if the point is inside the triangle
        x_offset: int = mouse_point[0] - self.x
        y_offset: int = mouse_point[1] - self.y

        if x_offset == 0:
            return True

        point_slope_from_y_intercept: float = (y_offset - self.height) / x_offset   # rise over run

        if point_slope_from_y_intercept < 1:
            return True

        else:
            return False

    def get_area(self) -> int | float:
        the_area: float = .5 * self.width * self.height

        return the_area

    def draw(self) -> None:
        pygame.draw.polygon(self.window, self.color,
                            ((self.x, self.y + self.height),
                             (self.x, self.y),
                             (self.x + self.width, self.y)))
