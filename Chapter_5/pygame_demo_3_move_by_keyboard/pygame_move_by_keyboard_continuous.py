# pygame_move_by_keyboard_continuous.py

# pygame demo 3(b) - one image, continuous mode, move as long as a key is down

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
MAX_WIDTH: int = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT: int = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

TARGET_X: int = 400
TARGET_Y: int = 320
TARGET_WIDTH_HEIGHT: int = 120
N_PIXELS_TO_MOVE: int = 3

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets:  image(s0, sound(s), etc.
ball_image: pygame.Surface = pygame.image.load("images/ball.png")
target_image: pygame.Surface = pygame.image.load("images/target.jpg")

# 5 - Initialize variables
ball_x: int = random.randrange(MAX_WIDTH)
ball_y: int = random.randrange(MAX_HEIGHT)
target_rect: pygame.Rect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    # Check for user pressing keys
    key_pressed_tuple: type[pygame.key] = pygame.key.get_pressed()

    if key_pressed_tuple[pygame.K_LEFT]:    # moving left
        ball_x -= N_PIXELS_TO_MOVE

    if key_pressed_tuple[pygame.K_RIGHT]:   # moving right
        ball_x += N_PIXELS_TO_MOVE

    if key_pressed_tuple[pygame.K_UP]:      # moving up
        ball_y -= N_PIXELS_TO_MOVE

    if key_pressed_tuple[pygame.K_DOWN]:    # moving down
        ball_y += N_PIXELS_TO_MOVE

    # Check if the ball is colliding with the target
    ball_rect: pygame.Rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    if ball_rect.colliderect(target_rect):
        print("Ball is touching the target")

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    window.blit(target_image, (TARGET_X, TARGET_Y))    # draw the target
    window.blit(ball_image, (ball_x, ball_y))  # draw the ball

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)   # make pygame wait
