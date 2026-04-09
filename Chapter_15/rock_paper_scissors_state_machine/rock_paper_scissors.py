# rock_paper_scissors.py

# Rock, Paper, Scissors in pygame
# Demonstration of a state machine

# 1 - Import packages
import pygame
from pygame.mixer import Sound
from pygwidgets import DisplayText, Image, CustomButton,ImageCollection
from random import choice
import sys


# 2 - Define constants
GRAY: tuple[int, int, int] = (100, 100, 100)
WHITE: tuple[int, int, int] = (255, 255, 255)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30

ROCK: str = "Rock"
PAPER: str = "Paper"
SCISSORS: str = "Scissors"

# Set constants for each of the three states
STATE_SPLASH: str = "Splash"
STATE_PLAYER_CHOICE: str = "PlayerChoice"
STATE_SHOW_RESULTS: str = "ShowResults"

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# For Splash screen
message_field: DisplayText = DisplayText(window, (15 ,25), "Welcome to Rock, Paper, Scissors!",
                                         fontSize=50, textColor=WHITE, width=610,justified="center")

rock_image: Image = Image(window, (25, 120), "images/Rock.png")
paper_image: Image = Image(window, (225, 120), "images/Paper.png")
scissors_image: Image = Image(window, (425, 120), "images/Scissors.png")

start_button: CustomButton = CustomButton(window, (210, 300),
                                          up="images/startButtonUp.png",
                                          down="images/startButtonDown.png",
                                          over="images/startButtonHighlight.png")

# For Player Choice
rock_button: CustomButton = CustomButton(window, (25, 120),
                                         up="images/Rock.png",
                                         over="images/RockOver.png",
                                         down="images/RockDown.png")

paper_button: CustomButton = CustomButton(window, (225, 120),
                                         up="images/Paper.png",
                                         over="images/PaperOver.png",
                                         down="images/PaperDown.png")

scissors_button: CustomButton = CustomButton(window, (425, 120),
                                         up="images/Scissors.png",
                                         over="images/ScissorsOver.png",
                                         down="images/ScissorsDown.png")

choose_text: DisplayText = DisplayText(window, (15, 395), "Choose!",
                                       fontSize=50, textColor=WHITE, width=610, justified="center")

results_field: DisplayText = DisplayText(window, (20, 275), "",
                                         fontSize=50, textColor=WHITE, width=610, justified="center")

# For results
rps_collection_player: ImageCollection = ImageCollection(window, (170, 160),
                                                         {
                                                             ROCK: "images/Rock.png",
                                                             PAPER: "images/Paper.png",
                                                             SCISSORS: "images/Scissors.png"
                                                         }, "")

rps_collection_computer: ImageCollection = ImageCollection(window, (450, 160),
                                                         {
                                                             ROCK: "images/Rock.png",
                                                             PAPER: "images/Paper.png",
                                                             SCISSORS: "images/Scissors.png"
                                                         }, "")

restart_button: CustomButton = CustomButton(window, (220, 310),
                                            up="images/restartButtonUp.png",
                                            down="images/restartButtonDown.png",
                                            over="images/restartButtonHighlight.png")

player_score_counter: DisplayText = DisplayText(window, (15, 315), "Player Score:",
                                              fontSize=50, textColor=WHITE)

computer_score_counter: DisplayText = DisplayText(window, (300, 315), "Computer Score:",
                                                fontSize=50, textColor=WHITE)

# Sounds
winner_sound: Sound = Sound("sounds/ding.wav")
tie_sound: Sound = Sound("sounds/push.wav")
loser_sound: Sound = Sound("sounds/buzz.wav")

# 5 - Initialize variables
player_score: int = 0
computer_score: int = 0
state: str = STATE_SPLASH   # the starting state

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state == STATE_SPLASH:
            if start_button.handleEvent(event):
                state = STATE_PLAYER_CHOICE

        elif state == STATE_PLAYER_CHOICE:  # let the user choose
            player_choice: str = ""     # indicates no choice yet

            if rock_button.handleEvent(event):
                player_choice = ROCK
                rps_collection_player.replace(ROCK)

            elif paper_button.handleEvent(event):
                player_choice = PAPER
                rps_collection_player.replace(PAPER)

            elif scissors_button.handleEvent(event):
                player_choice = SCISSORS
                rps_collection_player.replace(SCISSORS)

            if player_choice != "":     # player has made a choice, make computer choice
                # Computer chooses from tuple of moves
                rps: tuple[str, str, str] = (ROCK, PAPER, SCISSORS)

                computer_choice: str = choice(rps)  # computer chooses
                rps_collection_computer.replace(computer_choice)

                # Evaluate the game
                if player_choice == computer_choice:  # tie
                    results_field.setValue("It is a tie!")
                    tie_sound.play()

                elif player_choice == ROCK and computer_choice == SCISSORS:
                    results_field.setValue("Rock breaks Scissors. You win!")
                    player_score += 1
                    winner_sound.play()

                elif player_choice == ROCK and computer_choice == PAPER:
                    results_field.setValue("Rock is covered by Paper. You lose.")
                    computer_score += 1
                    loser_sound.play()

                elif player_choice == SCISSORS and computer_choice == PAPER:
                    results_field.setValue("Scissors cuts Paper. You win!")
                    player_score += 1
                    winner_sound.play()

                elif player_choice == SCISSORS and computer_choice == ROCK:
                    results_field.setValue("Scissors crushed by Rock. You lose.")
                    computer_score += 1
                    loser_sound.play()

                elif player_choice == PAPER and computer_choice == ROCK:
                    results_field.setValue("Paper covers Rock. You win!")
                    player_score += 1
                    winner_sound.play()

                elif player_choice == PAPER and computer_choice == SCISSORS:
                    results_field.setValue("Paper is cut by Scissors. You lose.")
                    computer_score += 1
                    loser_sound.play()

                # Show the player's score
                player_score_counter.setValue(f"Your Score: {player_score}")

                # Show the computer's score
                computer_score_counter.setValue(f"Computer Score: {computer_score}")

                state = STATE_SHOW_RESULTS  # change state

        elif state == STATE_SHOW_RESULTS:
            if restart_button.handleEvent(event):
                state = STATE_PLAYER_CHOICE  # change state

        else:
            raise ValueError(f"Unknow value for state: {state}")

    # 8 - Do any "per frame" actions
    if state == STATE_PLAYER_CHOICE:
        message_field.setValue("       Rock             Paper         Scissors")

    elif state == STATE_SHOW_RESULTS:
        message_field.setValue("You                     Computer")

    # 9 - Clear the screen
    window.fill(GRAY)

    # 10 - Draw all screen elements
    message_field.draw()

    if state == STATE_SPLASH:
        rock_image.draw()
        paper_image.draw()
        scissors_image.draw()
        start_button.draw()

    # Draw player choices
    elif state == STATE_PLAYER_CHOICE:
        rock_button.draw()
        paper_button.draw()
        scissors_button.draw()
        choose_text.draw()

    # Draw the results
    elif state == STATE_SHOW_RESULTS:
        results_field.draw()
        rps_collection_player.draw()
        rps_collection_computer.draw()
        player_score_counter.draw()
        computer_score_counter.draw()
        restart_button.draw()

    else:
        raise ValueError(f"Unknown value for state: {state}")
        
    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)   # make pygame wait
