# pygame_one_ball_bounce_x_y.py

# pygame demo 4(a) - one image, bounce around the window using (x, y) coordinates

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK: tuple[int] = (0, 0, 0)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30

BALL_WIDTH_HEIGHT: int = 100
N_PIXELS_PER_FRAME: int = 3

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets:  image(s0, sound(s), etc.
ball_image: pygame.Surface = pygame.image.load("images/ball.png")

# 5 - Initialize variables
MAX_WIDTH: int = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT: int = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ball_x: int = random.randrange(MAX_WIDTH)
ball_y: int = random.randrange(MAX_HEIGHT)

x_speed: int = N_PIXELS_PER_FRAME
y_speed: int = N_PIXELS_PER_FRAME

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    if (ball_x < 0) or (ball_x >= MAX_WIDTH):
        x_speed *= -1   # reverse X direction

    if (ball_y < 0) or (ball_y >= MAX_HEIGHT):
        y_speed *= -1   # reverse Y direction

    # Update the ball's location, using the speed in two directions
    ball_x += x_speed
    ball_y += y_speed

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    window.blit(ball_image, (ball_x, ball_y))

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
