# square.py

# Square class

from tile import *


class Square:
    """
    A Square is a square area of the game board, in the application window.
    Each square has a location, rectangle, a tuple of legal moves, and a
    Tile that is drawn on the Square.  For each user move, the game tells
    the clicked on Square to exchange its Tile with the blank (empty space) Square.
    """
    o_tile: Tile
    def __init__(self, window: pygame.Surface, left: int,
                 top: int, square_number: int, legal_moves_tuple: tuple[int, ...]) -> None:
        self.window: pygame.Surface = window
        self.rect: pygame.Rect = pygame.Rect(left, top, SQUARE_WIDTH, SQUARE_HEIGHT)
        self.square_number: int = square_number
        self.legal_moves_tuple: tuple[int, ...] = legal_moves_tuple
        self.loc: tuple[int, int] = (left, top)
        self.reset()

    def reset(self) -> None:
        # Create starting Tile associated with this Square
        self.o_tile: Tile = Tile(self.window, self.square_number)

    def is_tile_in_proper_place(self) -> bool:
        tile_number: int = self.o_tile.get_tile_number()

        return self.square_number == tile_number

    def get_legal_moves(self) -> tuple[int, ...]:
        return self.legal_moves_tuple

    def clicked_inside(self, mouse_loc: tuple[int, int]) -> bool:
        hit: bool = self.rect.collidepoint(mouse_loc)

        return hit

    def get_square_number(self) -> int:
        return self.square_number

    def switch(self, o_other_square: Square) -> None:
        # Switch the Tiles associated with two Square objects
        self.o_tile, o_other_square.o_tile = o_other_square.o_tile, self.o_tile

    def draw(self) -> None:
        # Tell the Tile to draw at the Square's location
        self.o_tile.draw(self.loc)
