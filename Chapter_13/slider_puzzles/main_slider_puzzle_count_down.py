# main_slider_puzzle_count_down.py

# Slider Puzzle Game with Count Down Timer

# 1 - Import packages
import pygwidgets
from pygame.constants import MOUSEBUTTONDOWN
from pyghelpers import CountDownTimer
import sys
from game import *

# 2 - Define constants
WINDOW_WIDTH: int = 470
WINDOW_HEIGHT: int = 560
FRAMES_PER_SECOND: int = 30
GAME_TIME: int = 180

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.
restart_button: pygwidgets.CustomButton = pygwidgets.CustomButton(window, (320, 455),
                                                                  up="images/restartButtonUp.jpg",
                                                                  down="images/restartButtonDown.jpg",
                                                                  over="images/restartButtonOver.jpg")

# 5 - Initialize variables
timer_display: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (50, 465), "",
                                                               fontSize=36, textColor=WHITE)

message_display: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (50, 510), "Click on tile to move it,",
                                                                 fontSize=36, textColor=WHITE)

o_game: Game = Game(window)     # create the main game object
sound_buzz: pygame.mixer.Sound = pygame.mixer.Sound("sounds/buzz.wav")

o_counter_down_timer: CountDownTimer = CountDownTimer(GAME_TIME)  # create a countdown clock timer
o_counter_down_timer.start()    # start the clock running

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            message_display.setText("")
            o_game.got_click(event.pos)
            over: bool = o_game.check_for_win()

            if over:
                message_display.setText("Grat job!!!")
                o_counter_down_timer.stop()

        if restart_button.handleEvent(event):
            o_game.start_new_game()
            o_counter_down_timer.start()

    # 8 - Do any "per frame" actions
    time_to_show: str = o_counter_down_timer.getTimeInHHMMSS(2)    # ask the Timer object for the elapsed time
    timer_display.setValue(f"Time: {time_to_show}")     # put that into a text field

    if o_game.get_game_playing():
        if o_counter_down_timer.ended():
            sound_buzz.play()
            message_display.setValue("Doh! You ran out of time.")
            o_game.stop_playing()

    # 9 - Clear the screen
    window.fill(BLACK)

    # 10 - Draw all screen elements
    o_game.draw()
    restart_button.draw()

    timer_display.draw()
    message_display.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)   # make pygame wait
