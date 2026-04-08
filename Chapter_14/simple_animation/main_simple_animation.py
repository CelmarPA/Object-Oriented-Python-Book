# main_simple_animation.py

# Animation example
# Shows example of SimpleAnimation object

# 1 - Import packages
import pygame
import sys
import pygwidgets
from simple_animation import *


# 2 - Define constants
SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30
BG_COLOR: tuple[int, int, int] = (0, 128, 128)

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.
dinosaur_anim_tuple: tuple[str, ...] = (
    "images/Dinobike/f1.gif",
    "images/Dinobike/f2.gif",
    "images/Dinobike/f3.gif",
    "images/Dinobike/f4.gif",
    "images/Dinobike/f5.gif",
    "images/Dinobike/f6.gif",
    "images/Dinobike/f7.gif",
    "images/Dinobike/f8.gif",
    "images/Dinobike/f9.gif",
    "images/Dinobike/f10.gif"
)

# 5 - Initialize variables
o_dinosaur_animation: SimpleAnimation = SimpleAnimation(window, (22, 140), dinosaur_anim_tuple, .1)

o_play_button: pygwidgets.TextButton =  pygwidgets.TextButton(window, (20, 240), "Play")

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if o_play_button.handleEvent(event):
            o_dinosaur_animation.play()

    # 8 - Do any "per frame" actions
    o_dinosaur_animation.update()

    # 9 - Clear the screen
    window.fill(BG_COLOR)

    # 10 - Draw all screen elements
    o_dinosaur_animation.draw()
    o_play_button.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)   # make pygame wait
