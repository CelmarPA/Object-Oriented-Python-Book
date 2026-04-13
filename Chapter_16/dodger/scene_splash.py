# scene_splash.py

# Splash scene - first scene the user sees
from pygame import Surface
from pygame.event import Event
from pygame.key import ScancodeWrapper
from pygwidgets import Image, CustomButton
from pyghelpers import Scene
from constants import *


class SceneSplash(Scene):

    def __init__(self, window: Surface) -> None:
        self.window: Surface = window

        self.background_image: Image = Image(self.window, (0, 0), "images/splashBackground.jpg")

        self.dodger_image: Image = Image(self.window, (150, 30), "images/dodger.png")

        self.start_button: CustomButton = CustomButton(self.window, (250, 500),
                                                       up="images/startNormal.png",
                                                       down="images/startDown.png",
                                                       over="images/startOver.png",
                                                       disabled="images/startDisabled.png",
                                                       enterToActivate=True)

        self.quit_button: CustomButton = CustomButton(self.window, (30 ,650),
                                                      up="images/quitNormal.png",
                                                      down="images/quitDown.png",
                                                      over="images/quitOver.png",
                                                      disabled="images/quitDisabled.png")

        self.high_scores_button: CustomButton = CustomButton(self.window, (360, 650),
                                                             up="images/gotoHighScoresNormal.png",
                                                             down="images/gotoHighScoresDown.png",
                                                             over="images/gotoHighScoresOver.png",
                                                             disabled="images/gotoHighScoresDisabled.png")

    def getSceneKey(self) -> str:
        return SCENE_SPLASH

    def handleInputs(self, events_list: list[Event], key_pressed_list: list[ScancodeWrapper]) -> None:
        for event in events_list:
            if self.start_button.handleEvent(event):
                self.goToScene(SCENE_PLAY)

            elif self.quit_button.handleEvent(event):
                self.quit()

            elif self.high_scores_button.handleEvent(event):
                self.goToScene(SCENE_HIGH_SCORES)

    def draw(self):
        self.background_image.draw()
        self.dodger_image.draw()
        self.start_button.draw()
        self.quit_button.draw()
        self.high_scores_button.draw()
