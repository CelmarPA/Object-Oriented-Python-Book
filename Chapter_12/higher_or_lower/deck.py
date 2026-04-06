# deck.py

# Deck class

import random
from card import *


class Deck:
    SUIT_TUPLE: tuple['str', ...] = ("Diamonds", "Clubs", "Hearts", "Spades")

    # This dict maps each card rank to a value for a standard deck
    STANDARD_DICT: dict[str, int] = {
        "Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "Jack": 11, "Queen": 12, "King": 13
    }

    def __init__(self, window: pygame.Surface, rank_value_dict=None) -> None:
        # rank_value_dict defaults to STANDARD_DICT, but you can call it
        # with a different dict, e.g., a special dict for Blackjack

        if rank_value_dict is None:
            rank_value_dict = Deck.STANDARD_DICT

        self.starting_deck_list: list[Card] = []
        self.playing_deck_list: list[Card] = []

        for suit in Deck.SUIT_TUPLE:
            for rank, value in rank_value_dict.items():
                o_card = Card(window, rank, suit, value)
                self.starting_deck_list.append(o_card)

        self.shuffle()

    def shuffle(self) -> None:
        # Copy the starting deck and save it in the playing deck list
        self.playing_deck_list = self.starting_deck_list.copy()

        for o_card in self.playing_deck_list:
            o_card.conceal()

        random.shuffle(self.playing_deck_list)

    def get_card(self) -> Card:
        if len(self.playing_deck_list) == 0:
            raise IndexError("No more cards")

        # Pop one card off the deck and return it
        o_card: Card = self.playing_deck_list.pop()

        return o_card

    def return_card_to_deck(self, o_card: Card) -> None:
        # Put a card back into the deck
        self.playing_deck_list.insert(0, o_card)


if __name__ == "__main__":
    # Main code to test the Deck class

    # Constants
    WINDOW_WIDTH: int = 100
    WINDOW_HEIGHT: int = 100

    pygame.init()
    window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    o_deck: Deck = Deck(window)

    for i in range(1, 53):
        o_card: Card = o_deck.get_card()

        print(f"Name: {o_card.get_name()}   Value: {o_card.get_value()}")


    #  Optional code to show blackjack deck
    # print("BlackJack Deck:")
    # blackjack_dict: dict[str, int] = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    #                 "6":6, "7":7, "8": 8, "9":9, "10":10,
    #                 "Jack":10, "Queen":10, "King":10}
    #
    # o_blackjack_deck: Deck = Deck(window, rank_value_dict=blackjack_dict)
    #
    # for i in range(1, 53):
    #     o_card: Card = o_blackjack_deck.get_card()
    #     print('Name: ', o_card.get_name(), '  Value:', o_card.get_value())