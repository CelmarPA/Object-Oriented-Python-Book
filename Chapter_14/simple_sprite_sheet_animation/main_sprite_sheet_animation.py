# main_sprite_sheet_animation.py

# Shows example of SpriteSheetAnimation object

# 1 - Import packages
import pygame
import sys
import pygwidgets
from pygwidgets import SpriteSheetAnimation

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
sprite_sheet_image: str = "images/water_003.png"

# 5 - Initialize variables
o_water_animation: SpriteSheetAnimation = SpriteSheetAnimation(window=window, loc=(22, 140),
                                                               imagePath=sprite_sheet_image, nImages=50,
                                                               width=192, height=192, durationOrDurationsList=0.05)

o_play_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (60, 320), "Play")

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if o_play_button.handleEvent(event):
            o_water_animation.play()

    # 8 - Do any "per frame" actions
    o_water_animation.update()

    # 9 - Clear the screen
    window.fill(BG_COLOR)

    # 10 - Draw all screen elements
    o_water_animation.draw()
    o_play_button.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)   # make PyGame wait the correct amount
