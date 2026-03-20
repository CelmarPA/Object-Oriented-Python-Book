# monster_example.py

import random


class Monster:

    def __init__(self, n_rows: int, n_cols: int, max_speed: int):
        self.n_rows: int = n_rows        # save away
        self.n_cols: int = n_cols        # save away
        self.my_row: int = random.randrange(self.n_rows)    # chooses a random row
        self.my_col: int = random.randrange(self.n_cols)    # chooses a random col
        self.my_speed_x: int = random.randrange(-max_speed, max_speed + 1)   # chooses an X speed
        self.my_speed_y: int = random.randrange(-max_speed, max_speed + 1)   # chooses a Y speed

        # Set other instance variables like health, power, etc.

    def move(self):
        self.my_row: int = (self.my_row + self.my_speed_y) % self.n_rows
        self.my_col: int = (self.my_col + self.my_speed_x) % self.n_cols


N_MONSTERS: int = 20
N_ROWS: int = 100   # could be any size
N_COLS: int = 100   # could be any size
MAX_SPEED: int = 4

monster_list: list[Monster] = []    # start with an empty list

for i in range(N_MONSTERS):
    o_monster: Monster = Monster(N_ROWS, N_COLS, MAX_SPEED)     # create a Monster
    monster_list.append(o_monster)   # add Monster to our list

# Later, when playing the game ...

for o_monster in monster_list:
    o_monster.move()
