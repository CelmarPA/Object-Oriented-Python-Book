# higher_or_lower

import random

# Card constants
SUIT_TUPLE: tuple[str] = ("Spades", "Hearts", "Clubs", "Diamonds")
RANK_TUPLE: tuple[str] = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")

N_CARDS: int = 8


# Pass in a deck and this function returns a random card from the deck
def get_card(deck_list_in: list[dict]) -> dict:
    this_card = deck_list_in.pop() # pop one off the top of the deck and return

    return this_card


# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deck_list_in: list[dict]) -> list[dict]:
    deck_list_out = deck_list_in.copy()  # make a copy of the starting deck

    random.shuffle(deck_list_out)

    return  deck_list_out


# Main code
print("Welcome to Higher or Lower.")
print("You have to choose whether the next card to be shown will be higher or lower than the current card.")
print("Getting it right adds 20 points; get ist wrong and you lose 15 points.")
print("You have 50 points to start.")
print()

starting_deck_list: list[dict] = []

for suit in SUIT_TUPLE:
    for this_value, rank in enumerate(RANK_TUPLE):
        card_dict: dict = {"rank": rank, "suit": suit, "value": this_value + 1}

        starting_deck_list.append(card_dict)

score: int = 50

while True: # play multiple games
    print()

    game_deck_list: list[dict] = shuffle(starting_deck_list)

    current_card_dict: dict = get_card(game_deck_list)
    current_card_rank: str = current_card_dict["rank"]
    current_card_value: int = current_card_dict["value"]
    current_card_suit: str = current_card_dict["suit"]

    print(f"Starting card is: {current_card_rank} of {current_card_suit}")
    print()

    for card_number in range(0, N_CARDS):  # play one game of this many cards
        answer = input(f"Will the next card be higher or lower than {current_card_rank} of {current_card_suit}? "
                       f"enter h or l): ").casefold()  # force lowercase

        next_card_dict: dict = get_card(game_deck_list)
        next_card_rank: str = next_card_dict["rank"]
        next_card_value: int = next_card_dict["value"]
        next_card_suit: str = next_card_dict["suit"]

        print(f"Next card is {next_card_rank} of {next_card_suit}")

        if answer == "h":
            if next_card_value > current_card_value:
                print("You got it right, it was higher")
                score += 20

            else:
                print("Sorry, it was not higher")
                score -= 15

        elif answer == "l":
            if next_card_value < current_card_value:
                score += 20
                print("You got it right, it was lower")

            else:
                score -= 15
                print("Sorry, it was not lower")

        print(f"Your score is: {score}")
        print()

        current_card_rank = next_card_rank
        current_card_value = next_card_value  # don't need current suit


    go_again = input("To play again, press ENTER, or \"q\" to quit: ").lower()

    if go_again == "q":
        break

print("OK bye")
