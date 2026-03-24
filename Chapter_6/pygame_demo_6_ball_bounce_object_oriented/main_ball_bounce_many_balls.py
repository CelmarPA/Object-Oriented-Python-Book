# main_ball_bounce_many_balls.py

# pygame demo 6(b) - using the Ball class, bounce many balls

# Import packages
import sys

import pygame

from ball import *    # bring in the Ball class code


# 2 - Define constants
BLACK: tuple[int] = (0, 0, 0)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
N_BALLS: int = 3

# 5 - Initialize variables
ball_list: list[Ball] = []

for ball in range(N_BALLS):
    # Each time through the loop, create a Ball object
    o_ball: Ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ball_list.append(o_ball)  # append the new Ball to the list of Balls

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    for o_ball in ball_list:
        o_ball.update() # tell each Ball to update itself

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    for o_ball in ball_list:
        o_ball.draw()   # tell each Ball to draw itself

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
