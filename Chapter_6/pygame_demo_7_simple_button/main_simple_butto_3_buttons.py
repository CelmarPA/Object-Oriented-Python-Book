# main_simple_butto_3_buttons.py

# Pygame demo 7 - 3 SimpleButton test

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
o_button_a: SimpleButton = SimpleButton(window, (25, 30), "images/buttonAUp.png", "images/buttonADown.png")
o_button_b: SimpleButton = SimpleButton(window, (150, 30), "images/buttonBUp.png", "images/buttonBDown.png")
o_button_c: SimpleButton = SimpleButton(window, (275, 30), "images/buttonCUp.png", "images/buttonCDown.png")

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to each button, see if one has been
        if o_button_a.handle_event(event):
            print("User clicked button A.")

        elif o_button_b.handle_event(event):
            print("User clicked button B.")

        elif o_button_c.handle_event(event):
            print("User clicked button C.")

    # 8 - Do any "per frame" actions

    # 9 - Clear the window
    window.fill(GRAY)

    # 10 - Draw all window elements
    o_button_a.draw()
    o_button_b.draw()
    o_button_c.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
