# timer_event.py

# Timer using custom event

# 1 - Import packages
import pygame
import sys
import pygwidgets


# 2 - Define constants
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 240
FRAMES_PER_SECOND: int = 30
WHITE: tuple[int, int, int] = (255, 255, 255)
#TIMER_EVENT_ID: int = pygame.USEREVENT + 1  # pygame 1.x approach
TIMER_EVENT_ID: int = pygame.event.custom_type()  # new in pygame 2.0
TIMER_LENGTH: float = 2.5 # seconds

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

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if start_button.handleEvent(event):
            pygame.time.set_timer(TIMER_EVENT_ID, int(TIMER_LENGTH * 1000), True)
            start_button.disable()
            timer_message.show()
            print("Starting timer")

        if event.type == TIMER_EVENT_ID:
            start_button.enable()
            timer_message.hide()
            print("Timer ended by event")

        if click_me_button.handleEvent(event):
            print("Other button was clicked")

    # 8 - Do any "per frame" actions

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
    clock.tick(FRAMES_PER_SECOND)       # make PyGame wait the correct amount
