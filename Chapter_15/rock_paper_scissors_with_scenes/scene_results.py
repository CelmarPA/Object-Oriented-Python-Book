# scene_results.py

# The Results scene
# The player is shown the results of the current round

from pygame import Surface
from pygame.event import Event
from pygame.key import ScancodeWrapper
from pygame.mixer import Sound
from pygwidgets import ImageCollection, DisplayText, CustomButton
from pyghelpers import Scene

from constants import *


class SceneResults(Scene):

    def __init__(self, window: Surface) -> None:
        self.window: Surface = window

        self.player_score: int = 0
        self.computer_score: int = 0

        self.rps_collection_player: ImageCollection = ImageCollection(window, (170, 160),
                                                                      {
                                                                          ROCK: "images/Rock.png",
                                                                          PAPER: "images/Paper.png",
                                                                          SCISSORS: "images/Scissors.png"
                                                                      }, "")

        self.rps_collection_computer: ImageCollection = ImageCollection(window, (450, 160),
                                                                        {
                                                                            ROCK: "images/Rock.png",
                                                                            PAPER: "images/Paper.png",
                                                                            SCISSORS: "images/Scissors.png"
                                                                        }, "")

        self.you_computer_field: DisplayText = DisplayText(window, (22, 25), "You                     Computer",
                                                           fontSize=50, textColor=WHITE, width=610, justified="center")

        self.results_field: DisplayText = DisplayText(self.window, (20, 275), "",
                                                      fontSize=50, textColor=WHITE,
                                                      width=610, justified="center")

        self.restart_button: CustomButton = CustomButton(self.window, (220, 310),
                                                         up="images/restartButtonUp.png",
                                                         down="images/restartButtonDown.png",
                                                         over="images/restartButtonHighlight.png")

        self.player_score_counter: DisplayText = DisplayText(self.window, (86, 315), "Score:",
                                                             fontSize=50,  textColor=WHITE)

        self.computer_score_counter: DisplayText = DisplayText(self.window, (384, 315), "Score:",
                                                             fontSize=50, textColor=WHITE)

        # Sounds
        self.winner_sound: Sound = Sound("sounds/ding.wav")
        self.tie_sound: Sound = Sound("sounds/push.wav")
        self.loser_sound: Sound = Sound("sounds/buzz.wav")

    def getSceneKey(self) -> str:
        return SCENE_RESULTS

    def enter(self, data: dict[str, str]) -> None:
        # data is a dictionary (comes from Play scene) that looks like:
        #      {'player':playerChoice, 'computer':computerChoice}
        player_choice: str = data["player"]
        computer_choice: str = data["computer"]

        # Set the player and computer images
        self.rps_collection_player.replace(player_choice)
        self.rps_collection_computer.replace(computer_choice)

        # Evaluate the game's win/lose/tie conditions
        if player_choice == computer_choice:  # tie
            self.results_field.setValue("It is a tie!")
            self.tie_sound.play()

        elif player_choice == ROCK and computer_choice == SCISSORS:
            self.results_field.setValue("Rock breaks Scissors. You win!")
            self.player_score += 1
            self.winner_sound.play()

        elif player_choice == ROCK and computer_choice == PAPER:
            self.results_field.setValue("Rock is covered by Paper. You lose.")
            self.computer_score += 1
            self.loser_sound.play()

        elif player_choice == SCISSORS and computer_choice == PAPER:
            self.results_field.setValue("Scissors cuts Paper. You win!")
            self.player_score += 1
            self.winner_sound.play()

        elif player_choice == SCISSORS and computer_choice == ROCK:
            self.results_field.setValue("Scissors crushed by Rock. You lose.")
            self.computer_score += 1
            self.loser_sound.play()

        elif player_choice == PAPER and computer_choice == ROCK:
            self.results_field.setValue("Paper covers Rock. You win!")
            self.player_score += 1
            self.winner_sound.play()

        elif player_choice == PAPER and computer_choice == SCISSORS:
            self.results_field.setValue("Paper is cut by Scissors. You lose.")
            self.computer_score += 1
            self.loser_sound.play()

        # Show the player's and computer's scores.
        self.player_score_counter.setValue(f"Score: {self.player_score}")
        self.computer_score_counter.setValue(f"Score: {self.computer_score}")

    def handleInputs(self, events_list: list[Event], key_pressed_list: list[ScancodeWrapper]) -> None:
        for event in events_list:
            if self.restart_button.handleEvent(event):
                self.goToScene(SCENE_PLAY)

    # No need to include update method, defaults to inherited one which does nothing.

    def draw(self) -> None:
        self.window.fill(OTHER_GRAY)
        self.you_computer_field.draw()
        self.results_field.draw()
        self.rps_collection_player.draw()
        self.rps_collection_computer.draw()
        self.player_score_counter.draw()
        self.computer_score_counter.draw()
        self.restart_button.draw()
