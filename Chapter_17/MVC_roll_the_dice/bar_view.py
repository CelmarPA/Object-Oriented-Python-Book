# bar_view.py

from bin import *
from constants import *
from model import Model


class BarView:

    def __init__(self, window: Surface, o_model: Model) -> None:
        self.window: Surface = window
        self.o_model: Model = o_model

        self.o_roll_total: DisplayText = DisplayText(self.window, (50, 406), "Roll total:",
                                                     fontName="arial", fontSize=16, justified="right", width=80)

        self.o_count: DisplayText = DisplayText(self.window, (50, 441), "Count:",
                                                     fontName="arial", fontSize=16, justified="right", width=80)

        self.o_percent: DisplayText = DisplayText(self.window, (50, 471), "Percent:",
                                                     fontName="arial", fontSize=16, justified="right", width=80)

        self.o_bins_dict: dict[int, Bin] = {}

        # Possible rolls only go from 2 to 12
        for roll_rotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            o_bin: Bin = Bin(self.window, roll_rotal)
            self.o_bins_dict[roll_rotal] = o_bin

    def update(self) -> None:
        n_rounds: int
        results_dict: dict[int, int]
        percents_dict: dict[int, int]

        n_rounds, results_dict, percents_dict = self.o_model.get_rounds_rolls_percents()

        for roll_total in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            this_result: int = results_dict[roll_total]
            this_percent: float = percents_dict[roll_total]
            o_bin: Bin = self.o_bins_dict[roll_total]
            o_bin.update(n_rounds, this_result, this_percent)

    def draw(self) -> None:
        self.o_roll_total.draw()
        self.o_count.draw()
        self.o_percent.draw()

        for o_bin in self.o_bins_dict.values():
            o_bin.draw()
