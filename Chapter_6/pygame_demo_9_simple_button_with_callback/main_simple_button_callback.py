# main_simple_button_callback.py

# pygame demo 9 - 3-button test with callbacks

# 1 - Import packages
import pygame
from pygame.locals import *
from simple_button import *
import sys


#2 - Define constants
GRAY: tuple[int] = (200, 200, 200)
WINDOW_WIDTH: int = 400
WINDOW_HEIGHT: int = 100
FRAMES_PER_SECOND: int = 30

# Define a function to be used as a "callback"
def my_callback_function():
    print("User pressed Button B, called my_callback_function")

# Define a class with a method to be used as a "callback"
class CallBackTest:
    def __init__(self):
        pass

    def my_method(self):
        print("User pressed Button C, called myMethod of the CallBackTest object")

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
o_callback_test: CallBackTest = CallBackTest()

# Create instances of SimpleButton
# No call back
o_button_a: SimpleButton = SimpleButton(window, (25, 30),
                                        "images/buttonAUp.png",
                                        "images/buttonADown.png")
o_button_b: SimpleButton = SimpleButton(window, (150, 30),
                                        "images/buttonBUp.png",
                                        "images/buttonBDown.png",
                                        callback=my_callback_function)
o_button_c: SimpleButton = SimpleButton(window, (275, 30),
                                        "images/buttonCUp.png",
                                        "images/buttonCDown.png",
                                        callback=o_callback_test.my_method)

counter: int = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to the button, see if has been clicked on
        if o_button_a.handle_event(event):
            print("User pressed button A, handled in the main loop")

        # o_button_b and o_button_c have callbacks, no need to check result of these calls
        o_button_b.handle_event(event)

        o_button_c.handle_event(event)

    # 8 - Do any "per frame" actions
    counter += 1

    # 9 - Clear the window
    window.fill(GRAY)

    # 10 - Draw all window elements
    o_button_a.draw()
    o_button_b.draw()
    o_button_c.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
