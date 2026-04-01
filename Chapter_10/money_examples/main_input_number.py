# main_input_number.py

#  Money Input Number Example
#
#  demonstrates overriding inherited InputText methods
#

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from input_number import *


# 2 - Define constants
BACKGROUND_COLOR: tuple[int] = (0, 180, 180)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
title_content: str = "Demo of InputText and InputNumber fields"
title: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (0, 40), value=title_content, fontSize=36,
                                                       width=WINDOW_WIDTH, justified="center")

text_caption_content: str = "Input any text:"
input_text_caption: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (20, 150), value=text_caption_content,
                                                                    fontSize=24, width=190, justified="right")

o_input_text: pygwidgets.InputText = pygwidgets.InputText(window, (230, 150), "", width=150)
ok_button_text: pygwidgets.TextButton = pygwidgets.TextButton(window, (430, 150), "OK")

num_caption_content: str = "Input number only:"
input_number_caption: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (20, 250), value=num_caption_content,
                                                                      fontSize=24, width=190, justified="right")

o_input_number: InputNumber = InputNumber(window, (230, 250), "", width=150)
ok_button_number: pygwidgets.TextButton = pygwidgets.TextButton(window, (430, 250), "OK")

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pressing Return/Enter or clicking OK triggers action
        if o_input_text.handleEvent(event) or ok_button_text.handleEvent(event):
            the_text: str = o_input_text.getValue()
            print(f"Input text field contains: {the_text}")

        if o_input_number.handleEvent(event) or ok_button_number.handleEvent(event):
            try:    # see if any error remains
                the_text: str = o_input_number.getValue()

            except ValueError:
                o_input_number.setValue("(not a number)")

            else:    # input was OK
                print(f"Input number field contains: {the_text}")

    # 8  Do any "per frame" actions

    # 9 - Clear the screen
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw all screen elements
    title.draw()
    input_text_caption.draw()
    o_input_text.draw()
    ok_button_text.draw()
    input_number_caption.draw()
    o_input_number.draw()
    ok_button_number.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
