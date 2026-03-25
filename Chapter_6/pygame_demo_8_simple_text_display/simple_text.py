# simple_text.py

import pygame
from pygame.locals import *


class SimpleText:

    def __init__(self, window: pygame.Surface, loc: tuple[int], value: str, text_color: tuple[int]):
        pygame.font.init()
        self.window: pygame.Surface = window
        self.loc = loc

        self.font: pygame.font.Font = pygame.font.SysFont(None, 30)
        self.text_color: tuple[int] = text_color
        self.text: str = None    # so that the call to setText below force the creation of the text image
        self.set_value(value)
        self.text_surface: pygame.Surface = self.font.render(self.text, True, self.text_color)

    def set_value(self, new_text: str):
        if self.text == new_text:
            return  # nothing to change

        self.text: str = new_text   # save the new text
        self.text_surface: pygame.Surface = self.font.render(self.text, True, self.text_color)

    def draw(self):
        self.window.blit(self.text_surface, self.loc)
