# pygame_text_button_ball.py

# Pygame demo text and buttons

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
import pygwidgets

# 2 - Define constants
BLACK: tuple[int] = (0, 0, 0)
GRAY: tuple[int] = (128, 128, 128)
WHITE: tuple[int] = (255, 255, 255)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30
N_PIXELS_PER_FRAME: int = 3
BALL_WIDTH_HEIGHT: int = 100

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
o_ball: pygwidgets.Image = pygwidgets.Image(window, (0, 0), "images/ball.png")

ball_left: int = 0
ball_top: int = 0

MAX_WIDTH: int = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT: int = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ball_x: int = random.randrange(MAX_WIDTH)
ball_y: int = random.randrange(MAX_HEIGHT)
x_speed: int = N_PIXELS_PER_FRAME
y_speed: int = N_PIXELS_PER_FRAME

o_background: pygwidgets.Image = pygwidgets.Image(window, (0, 0), "images/background.jpg")

o_restart_button: pygwidgets.CustomButton = pygwidgets.CustomButton(window, (500, 430),
                                                                    up='images/restartUp.png',
                                                                    down='images/restartDown.png',
                                                                    over='images/restartOver.png',
                                                                    disabled='images/restartDisabled.png')

o_hit_me_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (500, 370), "Hit Me")

o_message_text_a: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (20, 50), "Here is some text",
                                                                  fontSize=36, textColor=WHITE)

o_message_text_b: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (20, 150),
                                                                  "Here is more text\nAnd more text\nAnd even more text",
                                                                  fontSize=36, textColor=WHITE, justified="center")

o_user_input_a: pygwidgets.InputText = pygwidgets.InputText(window, (20, 350), "",
                                                            fontSize=24, textColor=BLACK, backgroundColor=WHITE)

o_user_input_b: pygwidgets.InputText = pygwidgets.InputText(window, (20, 430), "", width=400,
                                                            fontSize=24, textColor=WHITE, backgroundColor=BLACK)

counter: int = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if o_restart_button.handleEvent(event):
            counter: int = 0

        if o_hit_me_button.handleEvent(event):
            print("Do not hit me")

        if o_user_input_a.handleEvent(event):
            user_text: str = o_user_input_a.getText()
            print(f"In the first field, the user entered: {user_text}")

        if o_user_input_b.handleEvent(event):
            user_text: str = o_user_input_b.getText()
            print(f"The the second field, the user entered: {user_text}")

    # 8 - Do any "per frame" actions
    counter += 1

    o_message_text_a.setValue(f"Here is some text.  Loop counter: {counter}")

    ball_left, ball_top = o_ball.getLoc()

    if (ball_left < 0) or (ball_left + BALL_WIDTH_HEIGHT >= WINDOW_WIDTH):
        x_speed *= -1   # reverse X direction

    if (ball_top < 0) or (ball_top + BALL_WIDTH_HEIGHT >= WINDOW_HEIGHT):
        y_speed *= -1   # reverse Y direction

    # Update the rectangle of the ball, based on the speed in two directions
    ball_left += x_speed
    ball_top += y_speed

    o_ball.setLoc((ball_left, ball_top))

    # 9 - Clear the window before drawing it again
    o_background.draw()     # draw a background image

    # 10 - Draw the window elements
    o_ball.draw()

    o_restart_button.draw()
    o_hit_me_button.draw()

    o_message_text_a.draw()
    o_message_text_b.draw()

    o_user_input_a.draw()
    o_user_input_b.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
