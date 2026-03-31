# input_number.py

# InputNumber class - allows the user to enter only numbers
#
# Demo of inheritance

import pygame
import pygwidgets
from typing import Callable


BLACK: tuple[int] = (0, 0, 0)
WHITE: tuple[int] = (255, 255, 255)

# Tuple of legal editing keys
LEGAL_KEY_TUPLE: tuple[int, ...] = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_HOME,
                                    pygame.K_END, pygame.K_DELETE, pygame.K_BACKSPACE,
                                    pygame.K_RETURN, pygame.K_KP_ENTER)

# Legal keys to be typed
LEGAL_UNICODE_CHARS: str = "01234567890.-"


#
# InputNumber inherits from InputText
#
class InputNumber(pygwidgets.InputText):

    def __init__(self, window: pygame.Surface, loc: tuple[int], value: str = "", font_name: str | None = None,
                 font_size: int = 24, width: int = 200, text_color: tuple[int] = BLACK,
                 background_color: tuple[int] = WHITE, focus_color: tuple[int] = BLACK, initial_focus: bool = False,
                 nick_name: str | None = None, callback: Callable | None = None, mask: None = None,
                 keep_focus_on_submit: bool = False, allow_floating_number: bool = True,
                 allow_negative_number: bool = True):

        self.allow_floating_number: bool = allow_floating_number
        self.allow_negative_number: bool = allow_negative_number

        # Call the __init__ method of our base class
        super().__init__(window=window, loc=loc, value=value, fontName=font_name, fontSize=font_size, width=width,
                         textColor=text_color, backgroundColor=background_color, focusColor=focus_color,
                         initialFocus=initial_focus, nickname=nick_name, callBack=callback, mask=mask,
                         keepFocusOnSubmit=keep_focus_on_submit)

    # Override handleEvent so we can filter for proper keys
    def handleEvent(self, event) -> bool:
        if event.type == pygame.KEYDOWN:
            # If it's not an editing or numeric key ignore it
            # Unicode value is only present on key down
            allowable_key = ((event.key in LEGAL_KEY_TUPLE) or (event.unicode in LEGAL_UNICODE_CHARS))

            if not allowable_key:
                return False

            if event.unicode == "-":    # user typed a minus sign
                if not self.allow_negative_number:
                    # If no negatives, don't pass it through
                    return False

                if self.cursorPosition > 0:
                    return False    # can't put minus sign after 1st char

                if "-" in self.text:
                    return False    # can't enter a second minus sign

            if event.unicode == ".":
                if not self.allow_floating_number:
                    # If no floats, don't pass the period through
                    return False

                if "."in self.text:
                    return False    # can't enter a second period

        # Allow the key to go through to the base class
        result: bool = super().handleEvent(event)

        return result

    def get_value(self) -> float | int:
        user_string: str = super().getValue()
        print(user_string)
        try:
            if self.allow_floating_number:
                return_value: float = float(user_string)

            else:

                return_value: int = int(user_string)

        except ValueError:
            raise ValueError("Entry is not a number, needs to have at least one digit.")

        return return_value
