# scene_play.py
import pygame.mouse
#  Play scene - the main game play scene
from pygame import Surface
from pygame.event import Event
from pygame.key import ScancodeWrapper
from pygame.mixer import Sound
from pygwidgets import Image, DisplayText, CustomButton, TextCheckBox
from pyghelpers import Scene, customYesNoDialog
from player import *
from baddies import *
from goodies import *
from constants import *


def show_custom_yes_no_dialog(the_window: Surface, the_text: str) -> bool| None:
    o_dialog_background: Image = Image(the_window, (40, 250), "images/dialog.png")

    o_prompt_display_text: DisplayText = DisplayText(the_window, (0, 290), the_text, width=WINDOW_WIDTH,
                                                     justified="center", fontSize=36)

    o_yes_button: CustomButton = CustomButton(the_window, (320, 370),
                                              "images/gotoHighScoresNormal.png",
                                              over="images/gotoHighScoresOver.png",
                                              down="images/gotoHighScoresDown.png",
                                              disabled="images/gotoHighScoresDisabled.png")

    o_no_button: CustomButton = CustomButton(the_window, (62, 370),
                                             "images/noThanksNormal.png",
                                             over="images/noThanksOver.png",
                                             down="images/noThanksDown.png",
                                             disabled="images/noThanksDisabled.png")

    choice_as_boolean: bool | None = customYesNoDialog(the_window, o_dialog_background, o_prompt_display_text,
                                                       o_yes_button, o_no_button)

    return choice_as_boolean


BOTTOM_RECT: tuple[int, int, int, int] = (0, GAME_HEIGHT + 1, WINDOW_WIDTH, WINDOW_HEIGHT - GAME_HEIGHT)
STATE_WAITING: str = "waiting"
STATE_PLAYING: str = "playing"
STATE_GAME_OVER: str = "game over"


class ScenePlay(Scene):

    def __init__(self, window: Surface):
        self.window: Surface = window

        self.controls_background: Image = Image(self.window, (0, GAME_HEIGHT),
                                                "images/controlsBackground.jpg")

        self.quit_button: CustomButton = CustomButton(self.window, (30, GAME_HEIGHT + 90),
                                                      up="images/quitNormal.png",
                                                      down="images/quitDown.png",
                                                      over="images/quitOver.png",
                                                      disabled="images/quitDisabled.png")

        self.high_scores_button: CustomButton = CustomButton(self.window, (190, GAME_HEIGHT + 90),
                                                             up="images/gotoHighScoresNormal.png",
                                                             down="images/gotoHighScoresDown.png",
                                                             over="images/gotoHighScoresOver.png",
                                                             disabled="images/gotoHighScoresDisabled.png")

        self.new_game_button: CustomButton = CustomButton(self.window, (450, GAME_HEIGHT + 90),
                                                          up="images/startNewNormal.png",
                                                          down="images/startNewDown.png",
                                                          over="images/startNewOver.png",
                                                          disabled="images/startNewDisabled.png",
                                                          enterToActivate=True)

        self.sound_check_box: TextCheckBox = TextCheckBox(self.window, (430, GAME_HEIGHT + 17),
                                                          "Background music", True, textColor=WHITE)

        self.game_over_image: Image = Image(self.window, (140, 180), "images/gameOver.png")

        self.title_text: DisplayText = DisplayText(self.window, (70, GAME_HEIGHT + 17),
                                                   "Score:                                 High Score:",
                                                   fontSize=24, textColor=WHITE)

        self.score_text: DisplayText = DisplayText(self.window, (80, GAME_HEIGHT + 47), "0",
                                                   fontSize=36, textColor=WHITE, justified="right")

        self.high_score_text: DisplayText = DisplayText(self.window, (270, GAME_HEIGHT + 47), "",
                                                        fontSize=36, textColor=WHITE, justified="right")

        pygame.mixer.music.load("sounds/background.mid")
        self.ding_sound: Sound = Sound("sounds/ding.wav")
        self.game_over_sound: Sound = Sound("sounds/gameover.wav")

        # Instantiate objects
        self.o_player: Player = Player(self.window)
        self.o_baddie_mgr: BaddieMgr = BaddieMgr(self.window)
        self.o_goodie_mgr: GoodieMgr = GoodieMgr(self.window)

        self.highest_high_score: int = 0
        self.lowest_high_score: int = 0
        self.background_music: bool = True
        self.score: int = 0
        self.playing_state: str = STATE_WAITING


    def getSceneKey(self):
        return SCENE_PLAY

    def enter(self, data: dict) -> None:
        self.get_high_and_low_scores()

    def get_high_and_low_scores(self) -> None:
        # Ask the High Scores scene for a dict of scores
        # that looks like this:
        #  {"highest": highestScore, "lowest": lowestScore}]

        info_dict: dict[str, int] = self.request(SCENE_HIGH_SCORES, HIGH_SCORE_DATA)
        self.highest_high_score = info_dict["highest"]
        self.high_score_text.setValue(self.highest_high_score)
        self.lowest_high_score = info_dict["lowest"]

    def reset(self) -> None:     # start a new game
        self.score = 0
        self.score_text.setValue(self.score)
        self.get_high_and_low_scores()

        # Tell the managers to reset themselves
        self.o_baddie_mgr.reset()
        self.o_goodie_mgr.reset()

        if self.background_music:
            pygame.mixer.music.play(-1, 0.0)

        self.new_game_button.disable()
        self.high_scores_button.disable()
        self.sound_check_box.disable()
        self.quit_button.disable()

        pygame.mouse.set_visible(False)

    def handleInputs(self, events_list: list[Event], key_pressed_list: list[ScancodeWrapper]) -> None:
        if self.playing_state == STATE_PLAYING:
            return  # ignore button events while playing

        for event in events_list:
            if self.new_game_button.handleEvent(event):
                self.reset()
                self.playing_state = STATE_PLAYING

            if self.high_scores_button.handleEvent(event):
                self.goToScene(SCENE_HIGH_SCORES)

            if self.sound_check_box.handleEvent(event):
                self.background_music = self.sound_check_box.getValue()

            if self.quit_button.handleEvent(event):
                self.quit()

    def update(self) -> None:
        if self.playing_state != STATE_PLAYING:
            return  # only update when playing

        # Move the Player to the mouse position, get back its rect
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_rect: pygame.Rect = self.o_player.update(mouse_x, mouse_y)

        # Tell the GoodieMgr to move all Goodies
        # Returns the number of Goodies that the Player contacted
        n_goodies_hit = self.o_goodie_mgr.update(player_rect)
        if n_goodies_hit > 0:
            self.ding_sound.play()
            self.score += (n_goodies_hit * POINTS_FOR_GOODIES)

        # Tell the BaddieMgr to move all the Baddies
        # Returns the number of Baddies that fell off the bottom
        n_baddies_evaded = self.o_baddie_mgr.update()
        self.score += (n_baddies_evaded  * POINTS_FOR_BADDIE_EVADED)

        self.score_text.setValue(self.score)

        # Check if the Player has hit any Baddie
        if self.o_baddie_mgr.has_player_hit_baddie(player_rect):
            pygame.mouse.set_visible(True)
            pygame.mixer.music.stop()

            self.game_over_sound.play()
            self.playing_state = STATE_GAME_OVER
            self.draw()     # force drawing of game over message

            if self.score > self.lowest_high_score:
                score_string: str = f"Your Score: {self.score}\n"

                if self.score> self.highest_high_score:
                    dialog_text: str = f"{score_string} is a new high score, CONGRATULATIONS!"

                else:
                    dialog_text: str = f"{score_string} gets you on the high scores list."

                result = show_custom_yes_no_dialog(self.window, dialog_text)

                if result:
                    self.goToScene(SCENE_HIGH_SCORES, self.score)

            self.new_game_button.enable()
            self.high_scores_button.enable()
            self.sound_check_box.enable()
            self.quit_button.enable()

    def draw(self) -> None:
        self.window.fill(BLACK)

        # Tell the managers to draw all the Baddies and Goodies
        self.o_baddie_mgr.draw()
        self.o_goodie_mgr.draw()

        # Tell the Player to draw itself
        self.o_player.draw()

        # Draw all the info at the bottom of the window
        self.controls_background.draw()
        self.title_text.draw()
        self.score_text.draw()
        self.high_score_text.draw()
        self.sound_check_box.draw()
        self.quit_button.draw()
        self.high_scores_button.draw()
        self.new_game_button.draw()

        if self.playing_state == STATE_GAME_OVER:
            self.game_over_image.draw()

    def leave(self) -> None:
        pygame.mixer.music.stop()


        