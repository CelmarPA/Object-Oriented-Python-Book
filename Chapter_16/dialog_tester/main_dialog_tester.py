# main_dialog_tester.py

# Testing program for 6 dialog boxes

import sys
import os


# These lines are here just in case you are running from the command line
current_path: str = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)


# 1 - Import packages
import pygame
from pygame import Surface
from pygwidgets import Image, DisplayText, CustomButton, InputText, TextButton
from pyghelpers import customYesNoDialog, customAnswerDialog, textYesNoDialog, textAnswerDialog


# 2 - Define constants
BLACK: tuple[int, int, int] = (0, 0, 0)
BACKGROUND_COLOR: tuple[int, int, int] = (0, 138, 138)
WHITE: tuple[int, int, int] = (255, 255, 255)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30


# Intermediate functions
def show_custom_alert_dialog(the_window: Surface, the_text: str) -> bool | None:
    o_dialog_background: Image = Image(the_window, (60, 80), "images/dialog.png")

    o_prompt_display_text: DisplayText = DisplayText(the_window, (0, 150), the_text, width=WINDOW_WIDTH,
                                                     justified="center", fontSize=36)

    o_ok_button: CustomButton = CustomButton(the_window, (355, 235),
                                             "images/okNormal.png",
                                             over="images/okOver.png",
                                             down="images/okDown.png",
                                             disabled="images/okDisabled.png")

    response: bool | None = customYesNoDialog(the_window, o_dialog_background, o_prompt_display_text, o_ok_button, None)

    return response


def show_custom_yes_no_dialog(the_window: Surface, the_text: str) -> bool | None:
    o_dialog_background: Image = Image(the_window, (60, 80), "images/dialog.png")

    o_prompt_display_text: DisplayText = DisplayText(the_window, (0, 150), the_text, width=WINDOW_WIDTH,
                                                     justified="center", fontSize=36)

    o_no_button: CustomButton = CustomButton(the_window, (95, 235),
                                             "images/noNormal.png",
                                             over="images/noOver.png",
                                             down="images/noDown.png",
                                             disabled="images/noDisabled.png")

    o_yes_button: CustomButton = CustomButton(the_window, (355, 235),
                                             "images/yesNormal.png",
                                             over="images/yesOver.png",
                                             down="images/yesDown.png",
                                             disabled="images/yesDisabled.png")

    response: bool | None = customYesNoDialog(the_window, o_dialog_background, o_prompt_display_text,
                                              o_yes_button, o_no_button)

    return response


def show_custom_answer_dialog(the_window: Surface, the_text: str) -> str | None:
    o_dialog_background: Image = Image(the_window, (60, 80), "images/dialog.png")

    o_prompt_display_text: DisplayText = DisplayText(the_window, (0, 120), the_text, width=WINDOW_WIDTH,
                                                     justified="center", fontSize=36)

    o_user_input_text: InputText = InputText(the_window, (225, 165), "", fontSize=36, initialFocus=True)

    o_no_button: CustomButton = CustomButton(the_window, (95, 235),
                                             "images/cancelNormal.png",
                                             over="images/cancelOver.png",
                                             down="images/cancelDown.png",
                                             disabled="images/cancelDisabled.png")

    o_yes_button: CustomButton = CustomButton(the_window, (355, 235),
                                              "images/okNormal.png",
                                              over="images/okOver.png",
                                              down="images/okDown.png",
                                              disabled="images/okDisabled.png")

    response: str | None = customAnswerDialog(the_window, o_dialog_background, o_prompt_display_text, o_user_input_text,
                                              o_yes_button, o_no_button)

    return response


# 3 - Initialize the world
pygame.init()
window: Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
o_text_alert_button: TextButton = TextButton(window, (75,320), "Text Alert")
o_custom_alert_button: TextButton = TextButton(window, (75, 380), "Custom Alert")
o_text_yes_no_button: TextButton = TextButton(window, (280, 320), "Text Yes/No")
o_custom_yes_no_button: TextButton = TextButton(window, (280, 380), "Custom Yes/No")
o_text_answer_button: TextButton = TextButton(window, (485, 320), "Text Answer")
o_custom_answer_button: TextButton = TextButton(window, (485, 380), "Custom Answer")

o_title: DisplayText = DisplayText(window, (150, 25), "Click all buttons to test dialogs",
                                   fontSize=36, textColor=WHITE)

o_results: DisplayText = DisplayText(window, (20, 450), "", fontSize=36, textColor=WHITE, width=600)

# 6 - Loop forever
while True:

    # 7 -  Check for and handle events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()

        if o_text_alert_button.handleEvent(event):
            ignore: bool | None = textYesNoDialog(window, (75, 80, 500, 150), "This is an alert!",
                                                  "OK", None)
            o_results.setValue("User clicked the OK button")

        if o_custom_alert_button.handleEvent(event):
            ignore: bool | None = show_custom_alert_dialog(window, "This is an alert!")
            o_results.setValue("User clicked the OK button")

        if o_text_yes_no_button.handleEvent(event):
            returned_value: bool | None = textYesNoDialog(window, (75, 80, 500, 150),
                                                          "Do you want fries with that?")

            if returned_value:
                o_results.setValue("User clicked the Yes button")

            else:
                o_results.setValue("User clicked the No button")

        if o_custom_yes_no_button.handleEvent(event):
            returned_value: bool | None = show_custom_yes_no_dialog(window, "Dow you want fries with that?")

            if returned_value:
                o_results.setValue("User clicked the Yes button")

            else:
                o_results.setValue("User clicked the No button")

        if o_text_answer_button.handleEvent(event):
            user_answer: str | None = textAnswerDialog(window, (75, 80, 500, 200),
                                                       "What is your favorite flavor of ice cream?",
                                                       "Ok", "Cancel")

            if user_answer is not None:
                o_results.setValue(f"User clicked OK, text was: {user_answer}")

            else:
                o_results.setValue("User clicked Cancel")

        if o_custom_answer_button.handleEvent(event):
            user_answer: str | None = show_custom_answer_dialog(window, "What is your favorite flavor of ice cream?")

            if user_answer is not None:
                o_results.setValue(f"User clicked OK, text was: {user_answer}")

            else:
                o_results.setValue("User clicked Cancel")

    # 8 - Do any "per frame" actions

    # 9 - Clear the screen before drawing it again
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw the screen elements
    o_title.draw()
    o_text_alert_button.draw()
    o_custom_alert_button.draw()
    o_text_yes_no_button.draw()
    o_custom_yes_no_button.draw()
    o_text_answer_button.draw()
    o_custom_answer_button.draw()
    o_results.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)    # make pygame wait
