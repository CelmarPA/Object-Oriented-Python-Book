# elapsed_timer.py

# Timer in the main loop

# 1 - Import packages
import pygame
import sys
import pygwidgets
import time


# 2 - Define constants
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 240
WHITE: tuple[int, int, int] = (255, 255, 255)
FRAMES_PER_SECOND: int =  30
TIMER_LENGTH: float = 2.5

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
header_message: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (0, 50),
                                                                f'Click "Start" to start a {TIMER_LENGTH} '
                                                                f'second timer:', fontSize=36, justified="center",
                                                                width=WINDOW_WIDTH)

start_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (200, 100), "Start")

click_me_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (320, 100), "Click Me")

timer_message: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (0, 160), "Message showing during timer",
                                                               fontSize=36, justified="center", width=WINDOW_WIDTH)

timer_message.hide()
timer_running: bool = False
time_started: float = 0.0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if start_button.handleEvent(event):
            time_started = time.time()   # remember the start time
            start_button.disable()
            timer_message.show()
            print("Starting timer")
            timer_running = True

        if click_me_button.handleEvent(event):
            print("Other button was clicked")

    # 8 - Do any "per frame" actions
    if timer_running:    # if the timer is running
        elapsed: float = time.time() - time_started

        if elapsed >= TIMER_LENGTH: # True here means timer has ended
            start_button.enable()
            timer_message.hide()
            print("Timer ended by elapsed time")
            timer_running = False

    # 9 - Clear the screen
    window.fill(WHITE)

    # 10 - Draw all screen elements
    header_message.draw()
    start_button.draw()
    click_me_button.draw()
    timer_message.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
