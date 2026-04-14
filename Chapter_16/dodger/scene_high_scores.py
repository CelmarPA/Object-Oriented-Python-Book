# scene_high_scores.py

# High Scores scene

from pygame import Surface
from pygame.event import Event
from pygame.key import ScancodeWrapper
from pygwidgets import Image, DisplayText, InputText, CustomButton
from pyghelpers import customAnswerDialog, customYesNoDialog
from pyghelpers import Scene
from high_scores_data import *
from constants import *


def show_custom_answer_dialog(the_window: Surface, the_text: str) -> str | None:
    o_dialog_background: Image = Image(the_window, (35, 450), "images/dialog.png")

    o_prompt_display_text: DisplayText = DisplayText(the_window, (0, 480), the_text, width=WINDOW_WIDTH,
                                                     justified="center", fontSize=36)

    o_user_input_text: InputText = InputText(the_window, (200, 550), "", fontSize=36, initialFocus=True)

    o_no_button: CustomButton = CustomButton(the_window, (65, 595),
                                             "images/noThanksNormal.png",
                                             over="images/noThanksOver.png",
                                             down="images/noThanksDown.png",
                                             disabled="images/noThanksDisabled.png")

    o_yes_button: CustomButton = CustomButton(the_window, (330, 595),
                                              "images/addNormal.png",
                                              over="images/addOver.png",
                                              down="images/addDown.png",
                                              disabled="images/addDisabled.png")

    user_answer: str | None = customAnswerDialog(the_window, o_dialog_background, o_prompt_display_text,
                                                 o_user_input_text, o_yes_button, o_no_button)

    return user_answer


def show_custom_reset_dialog(the_window: Surface, the_text: str) -> bool | None:
    o_dialog_background: Image = Image(the_window, (35, 450), "images/dialog.png")

    o_prompt_display_text: DisplayText = DisplayText(the_window, (0, 480), the_text, width=WINDOW_WIDTH,
                                                     justified="center", fontSize=36)

    o_no_button: CustomButton = CustomButton(the_window, (65, 595),
                                             "images/cancelNormal.png",
                                             over="images/cancelOver.png",
                                             down="images/cancelDown.png",
                                             disabled="images/cancelDisabled.png")

    o_yes_button: CustomButton = CustomButton(the_window, (330, 595),
                                              "images/okNormal.png",
                                              over="images/okOver.png",
                                              down="images/okDown.png",
                                              disabled="images/okDisabled.png")

    choice_as_boolean: bool | None = customYesNoDialog(the_window, o_dialog_background, o_prompt_display_text,
                                                       o_yes_button, o_no_button)

    return choice_as_boolean


class SceneHighScores(Scene):

    def __init__(self, window: Surface) -> None:
        self.window: Surface = window
        self.o_high_scores_data: HighScoresData = HighScoresData()

        self.background_image: Image = Image(self.window, (0, 0), "images/highScoresBackground.jpg")

        self.names_field: DisplayText = DisplayText(self.window, (260, 84), "",
                                                    fontSize=48, textColor=BLACK,
                                                    width=300, justified="left")

        self.scores_field: DisplayText = DisplayText(self.window, (25, 84), "",
                                                     fontSize=48, textColor=BLACK,
                                                     width=175, justified="right")

        self.quit_button: CustomButton = CustomButton(self.window, (30, 650),
                                                      up="images/quitNormal.png",
                                                      down="images/quitDown.png",
                                                      over="images/quitOver.png",
                                                      disabled="images/quitDisabled.png")

        self.back_button: CustomButton = CustomButton(self.window, (240, 650),
                                                      up="images/backNormal.png",
                                                      down="images/backDown.png",
                                                      over="images/backOver.png",
                                                      disabled="images/backDisabled.png")

        self.reset_scores_button: CustomButton = CustomButton(self.window, (450, 650),
                                                              up="images/resetNormal.png",
                                                              down="images/resetDown.png",
                                                              over="images/resetOver.png",
                                                              disabled="images/resetDisabled.png")

        self.show_high_scores()

    def getSceneKey(self) -> str:
        return SCENE_HIGH_SCORES

    def enter(self, new_high_score_value: int | None = None) -> None:
        # This can be called two different ways:
        # 1. If no new high score, newHighScoreValue will be None
        # 2. newHighScoreValue is score of the current game - in top 10
        if new_high_score_value  is None:
            return  # nothing to do

        self.draw()     # draw before showing dialog
        # We have a new high score sent in from the Play scene
        dialog_question: str = f"To record your score of {new_high_score_value}\nplease enter your name:"
        player_name: str | None = show_custom_answer_dialog(self.window, dialog_question)

        if player_name is None:
            return  # user pressed Cancel

        # Add user adn score to high scores
        if player_name == "":
            player_name = "Anonymous"

        self.o_high_scores_data.add_high_score(player_name, new_high_score_value)

        # Show the updated high scores table
        self.show_high_scores()

    def show_high_scores(self) -> None:
        # Get the scores and names, show them in two fields
        scores_list: list[int]
        names_list: list[str]

        scores_list, names_list = self.o_high_scores_data.get_scores_and_names()

        self.names_field.setValue(names_list)
        self.scores_field.setValue(scores_list)

    def handleInputs(self, events_list: list[Event], key_pressed_list: list[ScancodeWrapper]) -> None:
        for event in events_list:
            if self.quit_button.handleEvent(event):
                self.quit()

            elif self.back_button.handleEvent(event):
                self.goToScene(SCENE_PLAY)

            elif self.reset_scores_button.handleEvent(event):
                confirmed: bool | None = show_custom_reset_dialog(self.window,
                                                                  "Are your sure you want to \nReset the high scores?")

                if confirmed:
                    self.o_high_scores_data.reset_scores()
                    self.show_high_scores()

    def draw(self):
        self.background_image.draw()
        self.scores_field.draw()
        self.names_field.draw()
        self.quit_button.draw()
        self.reset_scores_button.draw()
        self.back_button.draw()

    def respond(self, request_id: str) -> dict[str, int]:
        # Request from Play scene for the highest and lowest scores
        # Build a dictionary and return it to the Play scene
        highest_score: int
        lowest_score: int

        highest_score, lowest_score = self.o_high_scores_data.get_highest_and_lowest()

        return {"highest": highest_score, "lowest": lowest_score}
