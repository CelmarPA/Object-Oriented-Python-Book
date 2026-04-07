# count_up_timer_tester.py

# CountUpTimer Example

# 1 - Import packages
import pygame
import sys
import pygwidgets
from pyghelpers import CountUpTimer


# 2 - Define constants
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 240
FRAMES_PER_SECOND: int= 30
WHITE: tuple[int, int, int] = (255, 255, 255)

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
o_header_message: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (0, 50),
                                                                  "Click Start to start a timer:", fontSize=36,
                                                                  justified="center", width=WINDOW_WIDTH)

o_start_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (180, 100), "Start")

o_stop_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (320, 100), "Stop")

o_timer_message: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (66, 160), "get_time_in_seconds      get_time_in_HHMMSS",
                                                                 fontSize=36, width=WINDOW_WIDTH)

o_timer_display_seconds: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (220, 190), "",
                                                                         fontSize=36,  justified="right")

o_timer_display_HHMMSS: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (356, 190), "",
                                                                         fontSize=36,  justified="right")

o_timer_message.hide()    # start off with this message hidden

o_timer: CountUpTimer = CountUpTimer() # create a timer object

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if o_start_button.handleEvent(event):
            o_timer.start()     # start the timer
            o_start_button.disable()
            o_timer_message.show()
            print("Starting timer")

        if o_stop_button.handleEvent(event):
            print("Stop button was clicked")
            o_timer_message.hide()
            o_timer.stop()
            o_start_button.enable()

    # 8 - Do any "per frame" actions
    time_in_seconds: int = o_timer.getTimeInSeconds()
    time_in_HHMMSS: str = o_timer.getTimeInHHMMSS(2)
    o_timer_display_seconds.setValue(str(time_in_seconds))
    o_timer_display_HHMMSS.setValue(time_in_HHMMSS)

    # 9 - Clear the screen
    window.fill(WHITE)

    # 10 - Draw all screen elements
    o_header_message.draw()
    o_start_button.draw()
    o_stop_button.draw()
    o_timer_message.draw()
    o_timer_display_seconds.draw()
    o_timer_display_HHMMSS.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
