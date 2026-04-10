# constants.py

#
# Constants
#

from pygame.locals import *


NEXT_SCENE_EVENT: int = USEREVENT + 1

# Scene keys:
SCENE_SPLASH: str = 'splash'
SCENE_PLAY: str = 'play'
SCENE_RESULTS: str = 'results'

WHITE: tuple[int, int, int] = (255, 255, 255)
GRAY: tuple[int, int, int] = (100, 100, 100)
OTHER_GRAY: tuple[int, int, int] = (150, 150, 150)

ROCK: str = 'Rock'
PAPER: str = 'Paper'
SCISSORS: str = 'Scissors'
