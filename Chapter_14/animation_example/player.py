# player.py

# Player class

# 1 - Import packages
import pygame
from pygwidgets import AnimationCollection


PIXELS_PER_MOVE: int = 5

SOUTH: str = "south"
NORTH: str = "north"
WEST: str = "west"
EAST: str = "east"


class Player:

    n_pixels_per_move: int = 5

    def __init__(self, window: pygame.Surface, loc: tuple[int, int]) -> None:
        self.window: pygame.Surface = window
        self.loc: list[tuple[int, int]] = list(loc)

        walk_south_tuple: tuple[tuple[str, float], ...] = (
            ("images/player/walkF0.png", .1), ("images/player/walkF1.png", .1),
            ("images/player/walkF2.png", .1), ("images/player/walkF3.png", .1),
            ("images/player/walkF4.png", .1), ("images/player/walkF5.png", .1),
            ("images/player/walkF6.png", .1), ("images/player/walkF7.png", .1)
        )

        walk_north_tuple: tuple[tuple[str, float], ...] = (
            ("images/player/walkB0.png", .1), ("images/player/walkB1.png", .1),
            ("images/player/walkB2.png", .1), ("images/player/walkB3.png", .1),
            ("images/player/walkB4.png", .1), ("images/player/walkB5.png", .1),
            ("images/player/walkB6.png", .1), ("images/player/walkB7.png", .1)
        )

        walk_west_tuple: tuple[tuple[str, float], ...] = (
            ("images/player/walkL0.png", .1), ("images/player/walkL1.png", .1),
            ("images/player/walkL2.png", .1), ("images/player/walkL3.png", .1),
            ("images/player/walkL4.png", .1), ("images/player/walkL5.png", .1),
            ("images/player/walkL6.png", .1), ("images/player/walkL7.png", .1)
        )

        walk_east_tuple: tuple[tuple[str, float], ...] = (
            ("images/player/walkR0.png", .1), ("images/player/walkR1.png", .1),
            ("images/player/walkR2.png", .1), ("images/player/walkR3.png", .1),
            ("images/player/walkR4.png", .1), ("images/player/walkR5.png", .1),
            ("images/player/walkR6.png", .1), ("images/player/walkR7.png", .1)
        )

        self.o_walk_animations: AnimationCollection = AnimationCollection(window, self.loc,
                                                                          {
                                                                              SOUTH: walk_south_tuple,
                                                                              NORTH: walk_north_tuple,
                                                                              WEST: walk_west_tuple,
                                                                              EAST: walk_east_tuple
                                                                          },
                                                                          SOUTH, loop=True, autoStart=False)

        self.direction: str = SOUTH
        self.keys_down_list: list[str] = []
        self.is_moving: bool = False

    def get_rect(self) -> pygame.Rect:
        return self.o_walk_animations.getRect()

    def get_center_loc(self) -> tuple[int, int]:
        the_rect: pygame.Rect = self.get_rect()
        the_center: tuple[int, int] = the_rect.center

        return the_center

    def get_direction(self) -> str:
        return self.direction

    def handle_event(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.keys_down_list.append(SOUTH)
                self.direction = SOUTH
                self.o_walk_animations.replace(SOUTH)
                self.o_walk_animations.start()
                self.is_moving = True

            elif event.key == pygame.K_UP:
                self.keys_down_list.append(NORTH)
                self.direction = NORTH
                self.o_walk_animations.replace(NORTH)
                self.o_walk_animations.start()
                self.is_moving = True

            elif event.key == pygame.K_LEFT:
                self.keys_down_list.append(WEST)
                self.direction = WEST
                self.o_walk_animations.replace(WEST)
                self.o_walk_animations.start()
                self.is_moving = True

            elif event.key == pygame.K_RIGHT:
                self.keys_down_list.append(EAST)
                self.direction = EAST
                self.o_walk_animations.replace(EAST)
                self.o_walk_animations.start()
                self.is_moving = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.keys_down_list.remove(SOUTH)
            elif event.key == pygame.K_UP:
                self.keys_down_list.remove(NORTH)
            elif event.key == pygame.K_LEFT:
                self.keys_down_list.remove(WEST)
            elif event.key == pygame.K_RIGHT:
                self.keys_down_list.remove(EAST)

            if len(self.keys_down_list) == 0:
                self.o_walk_animations.stop()
                self.is_moving = False

            else:
                self.direction = self.keys_down_list[0]     # just use first keydown in list
                self.o_walk_animations.replace(self.direction)
                self.o_walk_animations.start()
                self.is_moving = True

    def update(self) -> tuple[int, int]:
        if self.is_moving:
            if self.direction == WEST:
                self.loc[0] -= Player.n_pixels_per_move

            elif self.direction == EAST:
                self.loc[0] += Player.n_pixels_per_move

            elif self.direction == NORTH:
                self.loc[1] -= Player.n_pixels_per_move

            elif self.direction == SOUTH:
                self.loc[1] += Player.n_pixels_per_move

            self.o_walk_animations.update()

        return self.loc[0], self.loc[1]

    def draw(self) -> None:
        self.o_walk_animations.draw()
