# scene_splash.py

#
# This is the Splash Scene
#
# This is where the player sees the intro screen
#

from pygame import Surface
from pygame.event import Event
from pygame.key import ScancodeWrapper
from pygwidgets import DisplayText, CustomButton, Image
from pyghelpers import Scene
from constants import *


class SceneSplash(Scene):

    def  __init__(self, window: Surface) -> None:
        self.window: Surface = window

        self.message_field: DisplayText = DisplayText(window, (15, 25), "Welcome to Rock, Paper, Scissors!",
                                                      fontSize=50, textColor=WHITE, width=610, justified="center")

        self.start_button: CustomButton = CustomButton(self.window, (210, 300),
                                                       up="images/startButtonUp.png",
                                                       down="images/startButtonDown.png",
                                                       over="images/startButtonHighlight.png")

        self.rock_image: Image = Image(window, (25, 120), "images/Rock.png")
        self.paper_image: Image = Image(window, (225, 120), "images/Paper.png")
        self.scissors_image: Image = Image(window, (425, 120), "images/Scissors.png")

    def getSceneKey(self) -> str:
        return SCENE_SPLASH

    def enter(self, data: dict) -> None:
        pass

    def handleInputs(self, events_list: list[Event], key_pressed_list: list[ScancodeWrapper]) -> None:
        for event in events_list:
            if self.start_button.handleEvent(event):
                self.goToScene(SCENE_PLAY)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.window.fill(GRAY)
        self.message_field.draw()
        self.rock_image.draw()
        self.paper_image.draw()
        self.scissors_image.draw()
        self.start_button.draw()

    def leave(self) -> None:
        return None
