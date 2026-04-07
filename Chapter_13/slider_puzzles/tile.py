# tile.py

# Tile class

import pygame
from constants import *


class Tile:

    """
    A Tile contains a tile number and an associated image
    """

    font: pygame.font.Font = pygame.font.SysFont(None, 60)

    def __init__(self, window: pygame.Surface, tile_number: int) -> None:
        self.window: pygame.Surface = window
        self.tile_number: int = tile_number

        # Use drawing calls to create a surface for each tile
        #   For the empty tile, just a filled tile
        #   For all others, draw a circle, and center a number in it
        #
        # Alternatively, we could load image tiles from a folder:
        # self.image = pygame.image.load('images/tile' + str(self.tileNumber + 1) + '.png')

        surface: pygame.Surface = pygame.Surface((SQUARE_WIDTH, SQUARE_HEIGHT))

        if self.tile_number == STARTING_OPEN_SQUARE_NUMBER:    # draw empty image
            surface.fill(GRAY)
            pygame.draw.rect(surface, BLACK, pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)), 2)   # black border around everything

        else:   # numbered image
            surface.fill(PURPLE)
            pygame.draw.rect(surface, BLACK, pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)), 2)   # black border around everything

            center_x: int = SQUARE_WIDTH // 2
            center_y: int = SQUARE_HEIGHT // 2

            pygame.draw.circle(surface, YELLOW, (center_x, center_y), 35)

            number_as_image: pygame.Surface = Tile.font.render(str(self.tile_number + 1), True, BLACK)
            width_of_number: int = number_as_image.get_width()
            left_pos: int = (SQUARE_WIDTH - width_of_number) // 2
            height_of_number: int = number_as_image.get_height()
            top_pos: int = (SQUARE_HEIGHT - height_of_number) // 2

            surface.blit(number_as_image, (left_pos, top_pos))

        self.image: pygame.Surface = surface

    def get_tile_number(self) -> int:
        return self.tile_number

    def draw(self, loc) -> None:
        self.window.blit(self.image, loc)
