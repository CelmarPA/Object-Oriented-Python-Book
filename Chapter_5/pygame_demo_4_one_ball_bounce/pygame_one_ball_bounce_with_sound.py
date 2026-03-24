# pygame_one_ball_bounce_rects.py

# pygame demo 4(b) - one image, bounce around the window using rects

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
N_PIXELS_PER_FRAME: int = 3

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ball_image: pygame.Surface = pygame.image.load("images/ball.png")

# 5 - Initialize variables
ball_rect: pygame.Rect = ball_image.get_rect()
MAX_WIDTH: int = WINDOW_WIDTH - ball_rect.width
MAX_HEIGHT: int = WINDOW_HEIGHT - ball_rect.height
ball_rect.left = random.randrange(MAX_WIDTH)
ball_rect.top = random.randrange(MAX_HEIGHT)
x_speed: int = N_PIXELS_PER_FRAME
y_speed: int = N_PIXELS_PER_FRAME

# Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    if (ball_rect.left < 0) or (ball_rect.right >= WINDOW_WIDTH):
        x_speed *= -1   # reverse X direction

    if (ball_rect.top < 0) or (ball_rect.bottom >= WINDOW_HEIGHT):
        y_speed *= -1   # reverse Y direction

    # Update the ball's rectangle using the speed in two directions
    ball_rect.left += x_speed
    ball_rect.top += y_speed

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    window.blit(ball_image, ball_rect)

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)

















