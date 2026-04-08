# animation_example.py

# Animation example
# Shows example of Animation object of pygwidgets

# 1 - Import packages
import pygame
import sys
import pygwidgets
from pygwidgets import Animation


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
dinosaur_anim_tuple_list: list[tuple[str, float]] = [
    ("images/Dinobike/f1.gif", 0.1),
    ("images/Dinobike/f2.gif", 0.1),
    ("images/Dinobike/f3.gif", 0.1),
    ("images/Dinobike/f4.gif", 0.1),
    ("images/Dinobike/f5.gif", 0.1),
    ("images/Dinobike/f6.gif", 0.1),
    ("images/Dinobike/f7.gif", 0.1),
    ("images/Dinobike/f8.gif", 0.1),
    ("images/Dinobike/f9.gif", 0.1),
    ("images/Dinobike/f10.gif", 0.1)
]

# 5 - Initialize variables
o_dinosaur_animation: Animation = Animation(window=window, loc=(22, 140), animTuplesList=dinosaur_anim_tuple_list)

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
