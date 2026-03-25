# simple_button.py
from typing import Callable

# SimpleButton class
#
# Uses a "state machine" approach
#

import pygame
from pygame.locals import *


class SimpleButton:
    # Used to track the state of the button
    STATE_IDLE: str = "idle"            # button is up, mouse not over button
    STATE_ARMED: str = "armed"          # button is down, mouse over button
    STATE_DISARMED: str = "disarmed"    # clicked down on button, rolled off

    def __init__(self, window: pygame.Surface, loc: tuple[int], up: str, down: str, callback: Callable = None):
        self.window: pygame.Surface = window
        self.loc: tuple[int] = loc
        self.surface_up: pygame.Surface = pygame.image.load(up)
        self.surface_down: pygame.Surface  = pygame.image.load(down)
        self.callback: Callable = callback

        # Get the rect of the button (used to see if the mouse is over the button)
        self.rect: pygame.Rect = self.surface_up.get_rect()
        self.rect[0]: int = loc[0]
        self.rect[1]: int = loc[1]

        self.state: str = SimpleButton.STATE_IDLE

    def handle_event(self, event_obj) -> bool:
        # This method will return True if user clicks the button.
        # Normally returns False.

        if event_obj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        event_point_in_button_rect = self.rect.collidepoint(event_obj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if (event_obj.type == MOUSEBUTTONDOWN) and event_point_in_button_rect:
                self.state: str = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if (event_obj.type == MOUSEBUTTONUP) and event_point_in_button_rect:
                self.state: str = SimpleButton.STATE_IDLE

                # If a callback was specified, call it back
                if self.callback is not None:
                    self.callback()

                return True    # clicked!

            if (event_obj.type == MOUSEMOTION) and (not event_point_in_button_rect):
                self.state: str = SimpleButton.STATE_DISARMED

        elif self.state == SimpleButton.STATE_DISARMED:
            if event_point_in_button_rect:
                self.state: str = SimpleButton.STATE_ARMED

            elif event_obj.type == MOUSEBUTTONUP:
                self.state: str = SimpleButton.STATE_IDLE

        return False

    def draw(self):
        # Draw the button's current appearance to the window
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surface_down, self.loc)

        else:   # IDLE or DISARMED
            self.window.blit(self.surface_up, self.loc)