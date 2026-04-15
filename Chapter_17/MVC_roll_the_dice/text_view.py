# text_view.py

#  TextChart - Roll The Dice

from pygame import Surface
from model import Model
from pygwidgets import DisplayText
from constants import *


class TextView:

    def __init__(self, window: Surface, o_model: Model) -> None:
        self.window: Surface = window
        self.o_model: Model = o_model

        total_text: list[str | int] = ["Roll Total", ""]

        for roll_total in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            total_text.append(roll_total)

        self.o_total_display: DisplayText = DisplayText(window, (200, 135), total_text,
                                                        fontSize=36, width=120, justified="right")

        self.o_count_display: DisplayText = DisplayText(window, (320, 135),
                                                        fontSize=36, width=120, justified="right")

        self.o_percent_display: DisplayText = DisplayText(window, (440, 135),
                                                          fontSize=36, width=120, justified="right")

    def update(self) -> None:
        n_rounds: int
        results_dict: dict[int, int]
        percents_dict: dict[int, int]

        n_rounds, results_dict, percents_dict = self.o_model.get_rounds_rolls_percents()

        count_list: list[str | int] = ["Count", ""]     # extra empty string for a blank line
        percent_list: list[str | int] = ["Percent", ""]

        for roll_total in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            count: int = results_dict[roll_total]
            percent: int = percents_dict[roll_total]

            count_list.append(count)

            # Build percent as a string with one decimal digit
            percent: str = f"{percent:.1%}"
            percent_list.append(percent)

        self.o_count_display.setValue(count_list)
        self.o_percent_display.setValue(percent_list)

    def draw(self) -> None:
        self.o_total_display.draw()
        self.o_count_display.draw()
        self.o_percent_display.draw()
