# goodies.py

# Goodie and GoodieMgr classes

import pygame
from pygame import Surface
from pygwidgets import Image
from random import randrange, choice
from constants import *


class Goodie:

    MIN_SIZE: int = 10
    MAX_SIZE: int = 40
    MIN_SPEED: int = 1
    MAX_SPEED: int = 8

    # Load the image once
    GOODIE_IMAGE: Surface = pygame.image.load("images/goodie.png")
    RIGHT: str = "right"
    LEFT: str = "left"

    def __init__(self, window: Surface) -> None:
        self.window: Surface = window
        size: int = randrange(Goodie.MIN_SIZE, Goodie.MAX_SIZE + 1)
        self.y: int = randrange(0, GAME_HEIGHT - size)

        self.direction: str = choice([Goodie.LEFT, Goodie.RIGHT])

        if self.direction == Goodie.LEFT:   # start on right side of the window
            self.x: int = WINDOW_WIDTH
            self.speed: int = - randrange(Goodie.MIN_SPEED, Goodie.MAX_SPEED + 1)
            self.min_left: int = - size

        else:   # start on left side of the window
            self.x = 0 - size
            self.speed = randrange(Goodie.MIN_SPEED, Goodie.MAX_SPEED + 1)

        self.image: Image = Image(self.window, (self.x, self.y), Goodie.GOODIE_IMAGE)

        percent: int = int((size * 100) / Goodie.MAX_SIZE)
        self.image.scale(percent, False)

    def update(self) -> bool:
        self.x += self.speed
        self.image.setLoc((self.x, self.y))

        if self.direction == Goodie.LEFT:
            if self.x < self.min_left:
                return True     # needs to be deleted

            else:
                return False    # stays in window

        else:
            if self.x > WINDOW_WIDTH:
                return True     # needs to be deleted

            else:
                return False    # stays in window

    def draw(self) -> None:
        self.image.draw()

    def collide(self, player_rect: pygame.Rect) -> bool:
        collide_with_player: bool = self.image.overlaps(player_rect)

        return collide_with_player


# GoodieMgr class
class GoodieMgr:

    GOODIE_RATE_LO: int = 90
    GOODIE_RATE_HI: int = 111

    goodies_list: list[Goodie]
    n_frames_til_next_goodie: int

    def __init__(self, window: Surface) -> None:
        self.window: Surface = window
        self.reset()

    def reset(self) -> None:    # Called when starting a new game
        self.goodies_list = []
        self.n_frames_til_next_goodie = GoodieMgr.GOODIE_RATE_HI

    def update(self, the_player_rect: pygame.Rect) -> int:
        # Tell each Goodie to update itself.
        # If a Goodie goes off an edge, remove it
        # Count up all Goodies that contact the player and remove them.
        n_goodies_hit: int = 0
        goodies_list_copy: list[Goodie] = self.goodies_list.copy()

        for o_goodie in goodies_list_copy:
            delete_me: bool = o_goodie.update()

            if delete_me:
                self.goodies_list.remove(o_goodie)

            elif o_goodie.collide(the_player_rect):
                self.goodies_list.remove(o_goodie)
                n_goodies_hit += 1

        # If the correct amount of frames has passed, add a new Goodie (and reset the counter)
        self.n_frames_til_next_goodie -= 1

        if self.n_frames_til_next_goodie == 0:
            o_goodie: Goodie = Goodie(self.window)
            self.goodies_list.append(o_goodie)
            self.n_frames_til_next_goodie = randrange(GoodieMgr.GOODIE_RATE_LO, GoodieMgr.GOODIE_RATE_HI)

        return n_goodies_hit

    def draw(self) -> None:
        for o_goodie in self.goodies_list:
            o_goodie.draw()
