# main_simple_sprite_sheet_animation_number.py

# Shows example of SimpleSpriteSheetAnimation object

# 1 - Import packages
import sys
import pygwidgets
from simple_sprite_sheet_animation import *

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
sprite_sheet_image: str = "images/numbers.png"

# 5 - Initialize variables
o_number_animation: SimpleSpriteSheetAnimation = SimpleSpriteSheetAnimation(window, (22, 140),
                                                                           sprite_sheet_image, 18, 64,
                                                                           64, 0.5)

o_play_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (60, 320), "Play")

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if o_play_button.handleEvent(event):
            o_number_animation.play()

    # 8 - Do any "per frame" actions
    o_number_animation.update()

    # 9 - Clear the screen
    window.fill(BG_COLOR)

    # 10 - Draw all screen elements
    o_number_animation.draw()
    o_play_button.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)   # make PyGame wait the correct amount
