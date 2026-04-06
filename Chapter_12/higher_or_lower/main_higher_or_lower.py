# main_higher_or_lower.py

# Higher or Lower - pygame version
# Main program

# 1 - Import packages
from pygame.locals import *
import sys
from game import *


# 2 - Define constants
WINDOW_WIDTH: int = 1000
WINDOW_HEIGHT: int = 600
FRAMES_PER_SECOND: int = 30

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.
background: pygwidgets.Image = pygwidgets.Image(window, (0, 0), "images/background.png")
new_game_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (20, 530), "New Game",
                                                               width=100, height=45)
higher_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (540, 520), "Higher",
                                                               width=120, height=55)
lower_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (340, 520), "Lower",
                                                               width=120, height=55)
quit_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (880, 530), "Quit",
                                                               width=100, height=45)

# 5 - Initialize variables
o_game: Game = Game(window)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if ((event.type == pygame.QUIT) or
            ((event.type == KEYDOWN) and (event.type == K_ESCAPE)) or
            (quit_button.handleEvent(event))):

            pygame.quit()
            sys.exit()

        if new_game_button.handleEvent(event):
            o_game.reset()
            lower_button.enable()
            higher_button.enable()

        if higher_button.handleEvent(event):
            game_over: bool = o_game.hit_high_or_lower(HIGHER)

            if game_over:
                higher_button.disable()
                lower_button.disable()

        if lower_button.handleEvent(event):
            game_over: bool = o_game.hit_high_or_lower(LOWER)

            if game_over:
                higher_button.disable()
                lower_button.disable()

    # 8 - Do any "per frame" actions

    # 9 - Clear the window before drawing it again
    background.draw()

    # 10 - Draw the window elements
    # Tell the game to draw itself
    o_game.draw()

    # Draw remaining user interface components
    new_game_button.draw()
    higher_button.draw()
    lower_button.draw()
    quit_button.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
