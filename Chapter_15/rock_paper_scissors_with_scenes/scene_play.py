# scene_play.py

# The Play scene
# The player chooses among rock, paper, or scissors

from pygame import Surface
from pygame.event import Event
from pygame.key import ScancodeWrapper
from pygwidgets import DisplayText, CustomButton
from pyghelpers import Scene
from constants import *
from random import choice


class ScenePlay(Scene):

    def __init__(self, window: Surface) -> None:
        self.window: Surface = window

        self.rps_tuple: tuple[str, str, str] = [ROCK, PAPER, SCISSORS]

        self.title_field: DisplayText = DisplayText(self.window, (15, 40), "    Rock               Paper          Scissors",
                                                    fontSize=50, textColor=WHITE, width=610, justified="center")

        self.message_field: DisplayText = DisplayText(self.window, (30, 395), "Choose!",
                                                      fontSize=50, textColor=WHITE, width=610, justified="center")

        self.rock_button: CustomButton = CustomButton(self.window, (25, 120),
                                                      up="images/Rock.png",
                                                      over="images/RockOver.png",
                                                      down="images/RockDown.png")

        self.paper_button: CustomButton = CustomButton(self.window, (225, 120),
                                                      up="images/Paper.png",
                                                      over="images/PaperOver.png",
                                                      down="images/PaperDown.png")

        self.scissors_button: CustomButton = CustomButton(self.window, (425, 120),
                                                          up="images/Scissors.png",
                                                          over="images/ScissorsOver.png",
                                                          down="images/ScissorsDown.png")

    def getSceneKey(self) -> str:
        return SCENE_PLAY

    def handleInputs(self, events_list: list[Event], key_pressed_list: list[ScancodeWrapper]) -> None:
        player_choice: str | None = None

        for event in events_list:
            if self.rock_button.handleEvent(event):
                player_choice = ROCK

            if self.paper_button.handleEvent(event):
                player_choice = PAPER

            if self.scissors_button.handleEvent(event):
                player_choice = SCISSORS

            if player_choice is not None:   # user has made a choice
                computer_choice: str = choice(self.rps_tuple)   # computer chooses
                data_dict = {"player": player_choice, "computer": computer_choice}
                self.goToScene(SCENE_RESULTS, data_dict)    # go to Results scene

    # No need to include update method, defaults to inherited one which does nothing

    def draw(self) -> None:
        self.window.fill(GRAY)
        self.title_field.draw()
        self.rock_button.draw()
        self.paper_button.draw()
        self.scissors_button.draw()
        self.message_field.draw()
