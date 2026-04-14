# high_scores_data.py

# HighScoresData class

from constants import *
from pathlib import Path
import json


class HighScoresData:
    """
    The data file is stored as a list of lists in JSON format.
    Each list is made up of a name and a score:
        [[name, score], [name, score], [name, score] ...]
    In this class, all scores are kept in self.scoresList
    The list is kept in order of scores, highest to lowest.
    """

    def __init__(self) -> None:
        self.BANK_SCORES_LIST: list[str | int] = [["-----", 0] for _ in range(N_HIGH_SCORES)]
        self.o_file_path: Path = Path("HighScores.json")

        # Try to open and load the data from the data file
        try:
            data: str = self.o_file_path.read_text()

        except FileNotFoundError:   # no file, set to blank scores and save
            self.reset_scores()
            return

        # File exists, load the scores from the JSON file
        self.scores_list: list[list[str | int]] = json.loads(data)

    def add_high_score(self, name: str, new_high_score: int) -> None:
        # Find the appropriate place to add the new high score
        place_found: bool = False

        for index, name_score_list in enumerate(self.scores_list):
            this_score: int = name_score_list[1]

            if new_high_score > this_score:
                # Insert into proper place, remove last entry
                self.scores_list.insert(index, [name, new_high_score])
                self.scores_list.pop(N_HIGH_SCORES)
                place_found = True
                break

        if not place_found:
            return      # score does not belong in the list

        # Save the updated scores
        self.save_scores()

    def save_scores(self) -> None:
        scores_as_json: str = json.dumps(self.scores_list)
        self.o_file_path.write_text(scores_as_json)

    def reset_scores(self):
        self.scores_list = self.BANK_SCORES_LIST.copy()

        self.save_scores()

    def get_scores_and_names(self) -> tuple[list[int], list[str]]:
        names_list: list[str] = []
        scores_list: list[int] = []

        for name_and_score in self.scores_list:
            this_name: str = name_and_score[0]
            this_score: int = name_and_score[1]

            names_list.append(this_name)
            scores_list.append(this_score)

        return scores_list, names_list

    def get_highest_and_lowest(self) -> tuple[int, int]:
        # Element 0 is highest entry, element -1 is the lowest
        highest_entry: list = self.scores_list[0]
        lowest_entry: list = self.scores_list[-1]

        # Get the score (element 1) of each sublist
        highest_score: int = highest_entry[1]
        lowest_score: int = lowest_entry[1]

        return highest_score, lowest_score
