# main_rock_paper_scissors.py

# Demo of Scenes with Scene manager
# Rock, Paper, Scissors

# 1 - Import packages
import pygame
from pyghelpers import SceneMgr
from scene_splash import *
from scene_play import *
from scene_results import *


# 2 - Define constants
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30

# 3 - Initialize the world
pygame.init()
window: Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
# Instantiate all scenes and store them into a list
scenes_list: list[Scene] = [
    SceneSplash(window),
    ScenePlay(window),
    SceneResults(window)
]

# Create the Scene Manager, passing in the scenes list, and FPS
o_scene_mgr: SceneMgr = SceneMgr(scenes_list, FRAMES_PER_SECOND)

# Tell the scene manager to start running
o_scene_mgr.run()
