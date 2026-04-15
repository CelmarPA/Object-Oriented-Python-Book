# main_mvc.py

#  Main MVC Roll The Dice - Irv Kalb

# 1 - Import packages
from controller import *


# 2 - Define constants
FRAMES_PER_SECOND: int = 30

# 3 - Initialize the world
pygame.init()
pygame.display.set_caption("Roll The Dice")
window: Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
# Instantiate the Controller object
o_controller: Controller = Controller(window)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass all events to the Controller
        o_controller.handle_event(event)

    # 8 - Do any "per frame" actions

    # 9 - Clear the screen

    # 10 - Draw all screen elements
    o_controller.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
