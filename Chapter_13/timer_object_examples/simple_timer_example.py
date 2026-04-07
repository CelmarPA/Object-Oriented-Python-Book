# simple_timer_example.py

# Simple timer example

# 1 - Import packages
import pygame
import sys
import pygwidgets
from pyghelpers import Timer


# 2 - Define constants
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 240
FRAMES_PER_SECOND: int= 30
WHITE: tuple[int, int, int] = (255, 255, 255)
TIMER_LENGTH: float = 2.5   # seconds

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


timer_message.hide()    # start off with this message hidden

o_timer: Timer = Timer(TIMER_LENGTH)     # create a Timer object

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if start_button.handleEvent(event):
            o_timer.start()     # start the timer
            start_button.disable()
            timer_message.show()
            print("Starting timer")

        if click_me_button.handleEvent(event):
            print("Other button was clicked")

    # 8 - Do any "per frame" actions
    if o_timer.update():    # True here means timer has ended
        start_button.enable()
        timer_message.hide()
        print("Timer ended")


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
    clock.tick(FRAMES_PER_SECOND)
