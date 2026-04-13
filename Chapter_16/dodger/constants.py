# constants.py

# Constants - used by multiple Python files

WINDOW_WIDTH: int = 600
WINDOW_HEIGHT: int = 700
GAME_HEIGHT: int = 560
DIALOG_BOX_OFFSET: int = 35
DIALOG_BOX_WIDTH: int = WINDOW_WIDTH - (2 * DIALOG_BOX_OFFSET)

# Scene Keys
SCENE_SPLASH: str = "scene splash"
SCENE_PLAY: str = "scene play"
SCENE_HIGH_SCORES: str = "scene high scores"

# Colors
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)

# Game specs
POINTS_FOR_GOODIES: int =  25
POINTS_FOR_BADDIE_EVADED: int = 1
HIGH_SCORE_DATA: str = "high score data"
N_HIGH_SCORES: int = 10
