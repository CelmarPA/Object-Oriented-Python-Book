# game.py

# Game class

from constants import *
from deck import *
from card import *


class Game:
    CARD_OFFSET: int = 110
    CARDS_TOP: int = 300
    CARDS_LEFT: int = 75
    N_CARDS: int = 8
    POINTS_CORRECT: int = 15
    POINTS_INCORRECT: int = 10

    def __init__(self, window: pygame.Surface) -> None:
        self.window: pygame.Surface = window
        self.o_deck: Deck = Deck(self.window)
        self.score: int = 100

        self.score_text: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (450, 164),
                                                                         f"Score: {self.score}",
                                                                         fontSize=36, textColor=WHITE,
                                                                         justified="right")

        self.message_text: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (50, 460),
                                                                           "", width=900, justified="center",
                                                                           fontSize=36, textColor=WHITE)

        self.loser_sound: pygame.mixer.Sound = pygame.mixer.Sound("sounds/loser.wav")
        self.winner_sound: pygame.mixer.Sound = pygame.mixer.Sound("sounds/ding.wav")
        self.card_shuffle_sound: pygame.mixer.Sound = pygame.mixer.Sound("sounds/cardShuffle.wav")
        self.card_flip_sound: pygame.mixer.Sound = pygame.mixer.Sound("sounds/cardFlip.wav")

        self.card_x_positions_list: list[int] = []
        this_left: int = Game.CARDS_LEFT

        # Calculate the x positions of all cards, once
        for card_num in range(Game.N_CARDS):
            self.card_x_positions_list.append(this_left)
            this_left += Game.CARD_OFFSET

        self.card_list: list[Card] | None = None
        self.card_number: int | None = None
        self.current_card_name: str | None = None
        self.current_card_value: int | None = None

        self.reset()     # start a round of the game

    def reset(self) -> None:    # this method is called when a new round starts
        self.card_shuffle_sound.play()
        self.card_list = []
        self.o_deck.shuffle()

        for card_index in range(Game.N_CARDS):
            o_card: Card = self.o_deck.get_card()
            self.card_list.append(o_card)
            this_x_position: int = self.card_x_positions_list[card_index]

            o_card.set_loc((this_x_position, Game.CARDS_TOP))

        self.show_card(0)
        self.card_number = 0
        self.score = 100
        self.score_text.setValue(f"Score: {self.score}")
        self.current_card_name, self.current_card_value = self.get_card_name_and_value(self.card_number)

        self.message_text.setValue(f"Starting card is {self.current_card_name}. Will the next card be higher or lower?")

    def get_card_name_and_value(self, index: int) -> tuple[str, int]:
        o_card: Card = self.card_list[index]
        the_name: str = o_card.get_name()
        the_value: int = o_card.get_value()

        return the_name, the_value

    def show_card(self, index: int) -> None:
        o_card: Card = self.card_list[index]

        o_card.reveal()

    def hit_high_or_lower(self, higher_or_lower: str) -> bool:
        self.card_number += 1
        self.show_card(self.card_number)

        next_card_name: str
        next_card_value: int
        next_card_name, next_card_value = self.get_card_name_and_value(self.card_number)

        if higher_or_lower == HIGHER:
            if next_card_value > self.current_card_value:
                self.score += Game.POINTS_CORRECT
                self.message_text.setValue(f"Yes, the {next_card_name} was higher")
                self.winner_sound.play()

            elif next_card_value < self.current_card_value:
                self.score -= Game.POINTS_INCORRECT
                self.message_text.setValue(f"No, the {next_card_name} was not higher")
                self.loser_sound.play()

            else:
                self.message_text.setValue(f"Ops, the {next_card_name} has the same value")
                self.card_flip_sound.play()

        elif higher_or_lower == LOWER:   # user hit the Lower button
            if next_card_value < self.current_card_value:
                self.score += Game.POINTS_CORRECT
                self.message_text.setValue(f"Yes, the {next_card_name} was lower")
                self.winner_sound.play()

            elif next_card_value > self.current_card_value:
                self.score -= Game.POINTS_INCORRECT
                self.message_text.setValue(f"No, the {next_card_name} was not lower")
                self.loser_sound.play()

            else:
                self.message_text.setValue(f"Ops, the {next_card_name} has the same value")
                self.card_flip_sound.play()

        self.score_text.setValue(f"Score: {self.score}")

        self.current_card_value = next_card_value   # set up for the next card

        done: bool = (self.card_number == (Game.N_CARDS - 1))    # did we reach the last card?

        return done

    def draw(self):
        # Tell each card to draw itself
        if self.card_list is not None:
            for o_card in self.card_list:
                o_card.draw()

        self.score_text.draw()
        self.message_text.draw()
