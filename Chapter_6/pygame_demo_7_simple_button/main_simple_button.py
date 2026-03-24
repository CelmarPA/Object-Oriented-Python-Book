# main_simple_button.py

# Pygame demo 7 - SimpleButton test

# Import packages
import sys
from simple_button import *


# 2 - Define constants
GRAY: tuple[int] = (200, 200, 200)
WINDOW_WIDTH: int = 400
WINDOW_HEIGHT: int = 100
FRAMES_PER_SECOND: int = 30

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables
# Create an instance of a SimpleButton
o_button: SimpleButton = SimpleButton(window, (150, 30), "images/buttonUp.png", "images/buttonDown.png")

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to the button, see if it has been clicked on
        if o_button.handle_event(event):
            print("User has clicked the button")

    # 8 - Do any "per frame" actions

    # 9 - Clear the window
    window.fill(GRAY)

    # 10 - Draw all window elements
    o_button.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
