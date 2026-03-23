# pygame_image_click_and_move.py

# pygame demo 2 - one image, click and move

# 1- Import packages
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
MAX_WIDTH: int = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT: int = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ball_image: pygame.Surface = pygame.image.load("images/ball.png")

# 5 - Initialize variables
ball_x: int = random.randrange(MAX_WIDTH)
ball_y: int = random.randrange(MAX_HEIGHT)
ball_rect: pygame.Rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # See if user clicked
        if event.type == pygame.MOUSEBUTTONUP:
            # mouse_x, mouse_y = event.pos # Could do this if we needed it
            # Check if the click was in the rect of the ball
            # If so, choose a random new location
            if ball_rect.collidepoint(event.pos):
                ball_x: int = random.randrange(MAX_WIDTH)
                ball_y: int = random.randrange(MAX_HEIGHT)
                ball_rect: pygame.Rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # 8 Do any "per frame" actions

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    # Draw the ball at the randomized location
    window.blit(ball_image, (ball_x, ball_y))

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
