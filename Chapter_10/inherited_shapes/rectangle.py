# rectangle.py

# Rectangle class

from shape import *

class Rectangle(Shape):

    def __init__(self, window: pygame.Surface, max_width: int, max_height: int):
        super().__init__(window, "Rectangle", max_width, max_height)

        self.width: int = random.randrange(10, 100)
        self.height: int = random.randrange(10, 100)
        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clicked_inside(self, mouse_point: tuple[int]) -> bool:
        clicked: bool = self.rect.collidepoint(mouse_point)

        return clicked

    def get_area(self) -> int | float:
        the_area: int = self.width * self.height

        return the_area

    def draw(self) -> None:
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
