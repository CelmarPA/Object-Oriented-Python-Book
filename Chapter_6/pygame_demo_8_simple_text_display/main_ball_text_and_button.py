# main_ball_text_and_button.py

# pygame demo 8 - SimpleText, SimpleButton, and Ball

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

from ball import *   # bring in the Ball class code
from simple_button import *
from simple_text import *

# 2 - Define constants
BLACK: tuple[int] = (0, 0, 0)
WHITE: tuple[int] = (255, 255, 255)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables
o_ball: Ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
o_frame_count_label: SimpleText = SimpleText(window, (60, 20), "Program has run through this many loops: ", WHITE)
o_frame_count_display: SimpleText = SimpleText(window, (500, 20), "", WHITE)
o_restart_button: SimpleButton = SimpleButton(window, (280, 60), "images/restartUp.png", "images/restartDown.png")
frame_counter: int = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            sys.exit()

        if o_restart_button.handle_event(event):
            frame_counter: int = 0  # clicked button, reset counter

    # 8 - Do any "per frame" actions
    o_ball.update()     # tell the ball to update itself
    frame_counter += 1  # increment each frame
    o_frame_count_display.set_value(str(frame_counter))

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    o_ball.draw()   # tell the ball to draw itself
    o_frame_count_label.draw()
    o_frame_count_display.draw()
    o_restart_button.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)

