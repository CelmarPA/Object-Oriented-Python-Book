# baddies.py

# Baddie and BaddieMgr classes

import pygame
from pygame import Surface
from pygwidgets import Image
from random import randrange
from constants import *


# Baddie class
class Baddie:

    MIN_SIZE: int = 10
    MAX_SIZE: int = 40
    MIN_SPEED: int = 1
    MAX_SPEED: int = 8

    # Load the image only once
    BADDIE_IMAGE: Surface = pygame.image.load("images/baddie.png")

    def __init__(self, window: Surface) -> None:
        self.window: Surface = window

        # Create the image object
        size: int = randrange(Baddie.MIN_SIZE, Baddie.MAX_SIZE + 1)
        self.x: int = randrange(0, WINDOW_WIDTH - size)
        self.y: int = 0 - size  # start above the window

        self.image: Image = Image(self.window, (self.x, self.y), Baddie.BADDIE_IMAGE)

        # Scale it
        percent: float = (size * 100) / Baddie.MAX_SIZE
        self.image.scale(percent, False)
        self.speed: int = randrange(Baddie.MIN_SPEED, Baddie.MAX_SPEED + 1)

    def update(self) -> bool:   # move the Baddie down
        self.y += self.speed
        self.image.setLoc((self.x, self.y))

        if self.y > GAME_HEIGHT:
            return True     # needs to be deleted

        else:
            return False    # stays in the window

    def draw(self) -> None:
        self.image.draw()

    def collide(self, player_rect: pygame.Rect) -> bool:
        collide_with_player: bool = self.image.overlaps(player_rect)
        return collide_with_player


# BaddieMgr class
class BaddieMgr:

    ADD_NEW_BADDIE_RATE: int = 8     # how often to add a new Baddie
    baddies_list: list[Baddie]
    n_frames_til_next_baddie: int

    def __init__(self, window: Surface) -> None:
        self.window: Surface = window
        self.reset()

    def reset(self) -> None:     # called when starting a new game
        self.baddies_list = []
        self.n_frames_til_next_baddie = BaddieMgr.ADD_NEW_BADDIE_RATE

    def update(self) -> int:
        # Tell each Baddie to update itself
        # Count how many Baddies have fallen off the bottom.
        n_baddies_removed: int = 0
        baddies_list_copy: list[Baddie] = self.baddies_list.copy()

        for o_baddie in baddies_list_copy:
            delete_me: bool = o_baddie.update()

            if delete_me:
                self.baddies_list.remove(o_baddie)
                n_baddies_removed += 1

        # Check if it's time to add a new Baddie
        self.n_frames_til_next_baddie -= 1

        if self.n_frames_til_next_baddie == 0:
            o_baddie: Baddie = Baddie(self.window)
            self.baddies_list.append(o_baddie)
            self.n_frames_til_next_baddie = BaddieMgr.ADD_NEW_BADDIE_RATE

        # Return that count of Baddies that were removed
        return n_baddies_removed

    def draw(self) -> None:
        for o_baddie in self.baddies_list:
            o_baddie.draw()

    def has_player_hit_baddie(self, player_rect: pygame.Rect) -> bool:
        for o_baddie in self.baddies_list:
            if o_baddie.collide(player_rect):
                return True

        return False
