# balloon.py

#  Balloon base class and 3 subclasses

import pygame
import random
import pygwidgets
from balloon_constants import *
from abc import ABC, abstractmethod


class Balloon(ABC):

    pop_sound_loaded: bool = False
    pop_sound: pygame.mixer.Sound = None     # load when first balloon is created
    squeak_sound: pygame.mixer.Sound = None

    @abstractmethod
    def __init__(self, window: pygame.Surface, max_width: int, max_height: int, id: int, o_image: pygwidgets.Image,
                 size: str, n_points: int, speed_y: float) -> None:
        self.window: pygame.Surface = window
        self.id: int = id
        self.balloon_image: pygwidgets.Image = o_image
        self.size: str = size
        self.n_points: int = n_points
        self.speed_y: int = speed_y

        if not Balloon.pop_sound_loaded:    # load first time only
            Balloon.pop_sound_loaded = True
            Balloon.pop_sound = pygame.mixer.Sound("sounds/balloonPop.wav")
            Balloon.squeak_sound = pygame.mixer.Sound("sounds/balloonSqueak.wav")

        balloon_rect: pygame.Rect = self.balloon_image.getRect()
        self.width: int = balloon_rect.width
        self.height: int = balloon_rect.height
        # Position so balloon is within the width of the window, but below the bottom
        self.x: int = random.randrange(max_width - self.width)
        self.y: float = max_height + random.randrange(75)
        self.balloon_image.setLoc((self.x, self.y))

    def clicked_inside(self, mouse_point: tuple[int, float]) -> tuple[bool, int]:
        my_rect: pygame.Rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if my_rect.collidepoint(mouse_point):
            Balloon.pop_sound.play()

            return True, self.n_points      # True here means it was hit

        else:
            return False, 0     # not hit, no points

    def update(self) -> str:
        self.y -= self.speed_y      # update y position by speed
        self.balloon_image.setLoc((self.x, self.y))

        if self.y < -self.height:   # off the top of the window
            return BALLOON_MISSED

        else:
            return BALLOON_MOVING

    def draw(self):
        self.balloon_image.draw()

    def __del__(self):
        print(f"{self.size} Balloon {self.id} is going away")


class BalloonSmall(Balloon):

    balloon_image: pygame.Surface = pygame.image.load("images/redBalloonSmall.png")

    def __init__(self, window:  pygame.Surface, max_width: int, max_height: int, id: int) -> None:
        o_image: pygwidgets.Image = pygwidgets.Image(window, (0, 0), BalloonSmall.balloon_image)

        super().__init__(window, max_width, max_height, id, o_image, "Small", 30, 3.1)


class BalloonMedium(Balloon):

    balloon_image: pygame.Surface = pygame.image.load("images/redBalloonMedium.png")

    def __init__(self, window: pygame.Surface, max_width: int, max_height: int, id: int) -> None:
        o_image: pygwidgets.Image = pygwidgets.Image(window, (0, 0), BalloonMedium.balloon_image)

        super().__init__(window, max_width, max_height, id, o_image, "Medium", 20, 2.2)


class BalloonLarge(Balloon):
    balloon_image: pygame.Surface = pygame.image.load("images/redBalloonLarge.png")

    def __init__(self, window: pygame.Surface, max_width: int, max_height: int, id: int) -> None:
        o_image: pygwidgets.Image = pygwidgets.Image(window, (0, 0), BalloonLarge.balloon_image)

        super().__init__(window, max_width, max_height, id, o_image, "Large", 10, 1.5)


class MegaBalloon(Balloon):
    balloon_image: pygame.Surface = pygame.image.load("images/megaBalloon.png")


    def __init__(self, window: pygame.Surface, max_width: int, max_height: int, id: int) -> None:
        self.o_image: pygwidgets.Image = pygwidgets.Image(window, (0, 0), MegaBalloon.balloon_image)
        self.count: int = 0
        super().__init__(window, max_width, max_height, id, self.o_image, "Mega",40, 10.5)

    def clicked_inside(self, mouse_point: tuple[int, float]) -> tuple[bool, int]:
        my_rect: pygame.Rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if my_rect.collidepoint(mouse_point):
            self.count += 1
            self.o_image.replace(f"images/megaBalloon{self.count}.png")
            Balloon.squeak_sound.play()

        if self.count == 3:
            Balloon.pop_sound.play()

            return True, self.n_points  # True here means it was hit

        else:
            return False, 0  # not hit, no points
