# game.py
# Game class

from square import *
import random


class Game:
    o_open_square: Square
    START_LEFT: int = 35
    START_TOP: int = 30

    def __init__(self, window: pygame.Surface) -> None:
        self.window: pygame.Surface = window

        """
        The game board is made up of 4 rows and 4 columns - 16 squares,
        with 15 labelled images (1 to 15) and a blank square image.
        However, because Python lists and tuples start at zero, the squares
        are internally numbered (indexed) 0 to 15, like this:
             0  1  2  3
             4  5  6  7
             8  9 10 11
            12 13 14 15
        (A Square is an area of the window, each contains a tile, which is movable.)

        The following is a dict of squareNumber:tuple.  Each tuple contains all
        moves (vertical and horizontal neighbors) that can switch with this square.
        For example, for Square 0, only Squares 1 and 4 are legal moves.
        """

        legal_moves_dict: dict[int, tuple[int, ...]] = {
            0: (1, 4),
            1: (0, 2, 5),
            2: (1, 3, 6),
            3: (2, 7),
            4: (0, 5, 8),
            5: (1, 4, 6, 9),
            6: (2, 5, 7, 10),
            7: (3, 6, 11),
            8: (4, 9, 12),
            9: (5, 8, 10, 13),
            10: (6, 9, 11, 14),
            11: (7, 10, 15),
            12: (8, 13),
            13: (9, 12, 14),
            14: (10, 13, 15),
            15: (11, 14)
        }

        y_pos: int = Game.START_TOP
        self.square_list: list[Square] = []


        # Create list of Square objects
        for row in range(4):
            x_pos: int = Game.START_LEFT
            for col in range(4):
                square_number: int = (row * 4) + col
                legal_moves_tuple: tuple[int, ...] = legal_moves_dict[square_number]
                o_square: Square = Square(self.window, x_pos, y_pos, square_number, legal_moves_tuple)
                self.square_list.append(o_square)
                x_pos += SQUARE_WIDTH

            y_pos += SQUARE_HEIGHT

        self.sound_tick: pygame.mixer.Sound = pygame.mixer.Sound("sounds/tick.wav")
        self.sound_applause: pygame.mixer.Sound = pygame.mixer.Sound("sounds/applause.wav")
        self.sound_nope: pygame.mixer.Sound = pygame.mixer.Sound("sounds/nope.wav")

        self.playing: bool = False
        self.start_new_game()

    def start_new_game(self) -> None:
        # Tell all Squares to reset themselves
        for o_square in self.square_list:
            o_square.reset()

        self.o_open_square: Square = self.square_list[STARTING_OPEN_SQUARE_NUMBER]

        for _ in range(200):     # make 200 arbitrary moves to randomize
            legal_moves_for_this_tile: tuple[int, ...] = self.o_open_square.get_legal_moves()
            next_move_number: tuple[int, ...] = random.choice(legal_moves_for_this_tile)
            o_square: Square = self.square_list[next_move_number]

            # switch the randomly chosen Square & the open Square
            self.switch(o_square, play_move_sound=False)

        self.playing = True

    def got_click(self, click_loc: tuple[int, int]) -> None:
        if not self.playing:
            return # game is over, waiting for Restart button

        for o_square in self.square_list:
            if o_square.clicked_inside(click_loc):
                square_number: int = o_square.get_square_number()
                # print('Got a mouseDown on square number:', squareNumber)
                legal_moves_for_open_square_tuple: tuple[int, ...] = self.o_open_square.get_legal_moves()
                legal_move: bool = square_number in legal_moves_for_open_square_tuple

                if legal_move:
                    self.switch(o_square, play_move_sound=True)

                else:    # illegal move (not next to the open space)
                    self.sound_nope.play()

                return

    def switch(self, o_square_to_switch: Square, play_move_sound: bool) -> None:
        o_square_to_switch.switch(self.o_open_square)

        # Re-assign the open square
        self.o_open_square = o_square_to_switch

        if play_move_sound:
            self.sound_tick.play()

    def check_for_win(self) -> bool:
        if not self.playing:
            return False

        for o_square in self.square_list:
            if not o_square.is_tile_in_proper_place():
                return False

        # All in proper place, game over
        self.playing = False
        self.sound_applause.play()

        return True

    def get_game_playing(self) -> bool:
        return self.playing

    def stop_playing(self) -> None:
        self.playing = False

    def draw(self):
        for o_square in self.square_list:
            o_square.draw()
