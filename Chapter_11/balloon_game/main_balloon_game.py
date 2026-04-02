# main_balloon_game.py

#  Balloon game main code

# 1 - Import packages
import sys
from balloon_manager import *


# 2 - Define constants
BLACK: tuple[int, int, int] = (0, 0, 0)
GRAY: tuple[int, int, int] = (200, 200, 200)
BACKGROUND_COLOR: tuple[int, int, int] = (0, 180, 180)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 640
PANEL_HEIGHT: int = 60
USABLE_WINDOW_HEIGHT: int = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND: int = 30

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.
o_score_display: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25),
                                                                 "Score: 0", textColor=BLACK,
                                                                 backgroundColor=None, width=140, fontSize=24)
o_status_display: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25),
                                                                  "", textColor=BLACK, backgroundColor=None,
                                                                  width=300, fontSize=24)
o_start_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10),
                                                              "Start")

# 5 - Initialize variables
o_balloon_mgr: BalloonMgr = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing: bool = False   # wait until user clicks Start

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    n_points_earned: int = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            o_balloon_mgr.handle_event(event)
            the_score: int = o_balloon_mgr.get_score()
            o_score_display.setValue(f"Score: {the_score}")

        elif o_start_button.handleEvent(event):
            o_balloon_mgr.start()
            o_score_display.setValue(f"Score: 0")
            playing = True
            o_start_button.disable()

    # 8 - Do any "per frame" actions
    if playing:
        o_balloon_mgr.update()
        n_popped: int = o_balloon_mgr.get_count_popped()
        n_missed: int = o_balloon_mgr.get_count_missed()
        o_status_display.setValue(f"Popped: {n_popped}    "
                                  f"Missed: {n_missed}    "
                                  f"Out of: {N_BALLOONS}")

        if (n_popped + n_missed) == N_BALLOONS:
            playing = False
            o_start_button.enable()

    # 9 - Clear the window
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw all window elements
    if playing:
        o_balloon_mgr.draw()

    pygame.draw.rect(window, GRAY, pygame.Rect(0, USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))
    o_score_display.draw()
    o_status_display.draw()
    o_start_button.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
