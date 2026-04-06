# card.py

# Card class

import pygame
import pygwidgets


class Card:

    BACK_OF_CARD_IMAGE: pygame.Surface = pygame.image.load("images/BackOfCard.png")

    def __init__(self, window: pygame.Surface, rank: str, suit: str, value: int) -> None:
        self.window: pygame.Surface = window
        self.rank: str = rank
        self.suit: str = suit
        self.card_name: str = f"{rank} of {suit}"
        self.value: int = value

        file_name: str = f"images/{self.card_name}.png"
        # Set some starting location; use setLoc below to change
        self.images: pygwidgets.ImageCollection = pygwidgets.ImageCollection(window, (0, 0),
                                                                             {
                                                                                 "front": file_name,
                                                                                 "back": Card.BACK_OF_CARD_IMAGE
                                                                             }, "back")

    def conceal(self) -> None:
        self.images.replace("back")

    def reveal(self) -> None:
        self.images.replace("front")

    def get_name(self) -> str:
        return self.card_name

    def get_value(self) -> int:
        return self.value

    def get_suit(self) -> str:
        return self.suit

    def get_rank(self) -> str:
        return self.rank

    def set_loc(self, loc: tuple[int, int]) -> None:    # call the setLoc method of the ImageCollection
        self.images.setLoc(loc)

    def get_loc(self) -> tuple[int, int]:      # get the location from the ImageCollection
        loc: tuple[int, int] = self.images.getLoc()

        return loc

    def draw(self) -> None:
        self.images.draw()
