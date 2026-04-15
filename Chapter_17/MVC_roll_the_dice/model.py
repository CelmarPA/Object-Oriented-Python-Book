# model.py

#  Model - Roll The Dice

from random import randrange
from constants import *

SIDES_PER_DIE: int = 6
SIDES_PER_DIE_PLUS_ONE: int = SIDES_PER_DIE + 1


# Model class
class Model:

    def __init__(self) -> None:
        self.n_rounds: int = 0
        self.rolls_dict: dict[int, int] = {}
        self.percents_dict: dict[int, int] = {}

    def generate_rolls(self, n_rounds: int) -> None:
        self.n_rounds = n_rounds
        self.rolls_dict = {}

        for total in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):    # Initialize all to zero
            self.rolls_dict[total] = 0

        # Roll two dice, add them up, increment the count in the dict
        for round_number in range(self.n_rounds):
            die_1: int = randrange(1, SIDES_PER_DIE_PLUS_ONE)
            die_2: int = randrange(1, SIDES_PER_DIE_PLUS_ONE)

            the_sum: int = die_1 + die_2

            self.rolls_dict[the_sum] += 1

        # Calculate  and save percentages in a dict
        self.percents_dict = {}
        for roll_total, count in self.rolls_dict.items():
            this_percent: float = count / self.n_rounds
            self.percents_dict[roll_total] = this_percent

    # All current views call this method to get all the data.
    def get_rounds_rolls_percents(self) -> tuple[int, dict[int, int], dict[int, int]]:
        return self.n_rounds, self.rolls_dict, self.percents_dict

    # The methods below aren't used right now, but are available for new views
    def get_number_of_rounds(self) -> int:
        return self.n_rounds

    def get_rolls(self) -> dict[int, int]:
        return self.rolls_dict

    def get_percents(self) -> dict[int, int]:
        return self.percents_dict
