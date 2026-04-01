# display_money.py

# DisplayMoney class - displays a number as an amount of money
#
# Demo of inheritance

import pygame
import pygwidgets


BLACK: tuple[int] = (0, 0, 0)


#  DisplayMoney class inherits from DisplayText class
class DisplayMoney(pygwidgets.DisplayText):

    def __init__(self, window: pygame.Surface, loc: tuple[int], value: str | None = None, font_name: str | None = None,
                 font_size: int = 24, width: int = 150, height: int | None = None, text_color: tuple[int] = BLACK,
                 background_color: tuple[int] | None = None, justified: str = "left", nickname: str | None = None,
                 currency_symbol: str = "$", currency_symbol_on_left: bool = True, show_cents: bool = True):

        self.currency_symbol: str = currency_symbol
        self.currency_symbol_on_left: bool = currency_symbol_on_left
        self.show_cents: bool = show_cents

        if value is None:
            value: float = 0.00

        # Call the __init__ method of our base class
        super().__init__(window=window, loc=loc, value=value, fontName=font_name, fontSize=font_size, width=width,
                         height=height, textColor=text_color, backgroundColor=background_color, justified=justified,
                         nickname=nickname)

    def set_value(self, money: str) -> float:
        if money == "":
            money: float = 0.00

        money: float = float(money)

        if self.show_cents:
            money: str = f"{money:,.2f}"

        else:
            money: str = f"{money:,.0f}"

        if self.currency_symbol_on_left:
            the_text: str = self.currency_symbol + money

        else:
            the_text: str = money + self.currency_symbol

        # Call the setValue method of our base class
        super().setValue(the_text)
