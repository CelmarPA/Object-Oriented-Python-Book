# bin.py

#  Bin - Roll The Dice

import pygame
from pygame import Rect, Surface
from pygwidgets import DisplayText


MAX_BAR_HEIGHT: int = 300
BAR_BOTTOM: int = 390
BAR_WIDTH: int = 30
BAR_COLOR: tuple[int, int, int] = (128, 128, 128)
COLUMN_LEFT_START: int = 30
COLUMN_OFFSET: int = 55


# Bins Class
class Bin:
    n_pixels_per_trial: float
    rect: Rect

    def __init__(self, window: Surface, bin_number: int) -> None:
        self.window: Surface = window
        self.pixels_per_counts: int = MAX_BAR_HEIGHT

        self.left: int = COLUMN_LEFT_START + (bin_number * COLUMN_OFFSET)
        self.o_bin_label: DisplayText = DisplayText(window, (self.left + 3, BAR_BOTTOM + 12), bin_number,
                                                    fontName="arial", fontSize=24, width=25, justified="center")

        self.o_bin_count: DisplayText = DisplayText(window, (self.left - 5, BAR_BOTTOM + 50), "",
                                                    fontName="arial", fontSize=18, width=50, justified="center")

        self.o_bin_percent: DisplayText = DisplayText(window, (self.left - 5, BAR_BOTTOM + 80), "",
                                                      fontName="arial", fontSize=18, width=50, justified="right")

    def update(self, n_rounds: int, count: int, percent: float) -> None:
        self.o_bin_count.setValue(count)
        percent: str = f"{percent:.1%}"
        self.o_bin_percent.setValue(percent)

        # force float here, use int when drawing rects
        # Calculate the real height, multiply by two to make it look better
        # All bars will certainly be less than 50%
        self.n_pixels_per_trial = float(MAX_BAR_HEIGHT) / n_rounds
        bar_height: int = int(count * self.n_pixels_per_trial) * 2

        self.rect = Rect(self.left, BAR_BOTTOM - bar_height, BAR_WIDTH, bar_height)

    def draw(self) -> None:
        pygame.draw.rect(self.window, BAR_COLOR, self.rect, 0)
        self.o_bin_label.draw()
        self.o_bin_count.draw()
        self.o_bin_percent.draw()
