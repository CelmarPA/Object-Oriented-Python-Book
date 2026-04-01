# main_money_example.py

# Money example
#
# Demonstrates overriding inherited DisplayText and InputText methods

# 1 - Import packages
import sys
from display_money import *
from input_number import *

# 2 - Define constants
BLACK: tuple[int] = (0, 0, 0)
BLACKISH: tuple[int] = (10, 10 ,10)
GRAY: tuple[int] = (128, 128, 128)
WHITE: tuple[int] = (255, 255, 255)
BACKGROUND_COLOR: tuple[int] = (0, 180, 180)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables
title_content: str = "Demo of InputNumber and DisplayMoney fields"
title: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (0, 40), value=title_content, fontSize=36,
                                                       width=WINDOW_WIDTH, justified="center")

caption_content: str = "Input money amount:"
input_caption: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (20, 150), value=caption_content, fontSize=24,
                                                               width=190, justified="right")

input_field: InputNumber = InputNumber(window, (230, 150), "", width=150, initial_focus=True)

ok_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (430, 150), "OK")

output_cap_1_content: str = "Output dollars &cents:"
output_caption_1: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (20, 300), value=output_cap_1_content,
                                                                  fontSize=24, width=190, justified="right")

money_field_1: DisplayMoney = DisplayMoney(window, (230, 300), "", text_color=BLACK, background_color=WHITE,
                                         width=150)

output_cap_2_content: str = "Output dollars only:"
output_caption_2: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (20, 400), value=output_cap_1_content,
                                                                  fontSize=24, width=190, justified="right")

money_field_2: DisplayMoney = DisplayMoney(window, (230, 400), "", text_color=BLACK, background_color=WHITE,
                                         width=150, show_cents=False)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pressing Return/Enter or clicking OK triggers action
        if input_field.handleEvent(event) or ok_button.handleEvent(event):
            try:
                the_value: str = input_field.getValue()

            except ValueError:
                input_field.setValue("(not a number)")

            else:
                the_text: str = str(the_value)
                money_field_1.set_value(the_text)
                money_field_2.set_value(the_text)

    # 8 Do any "per frame" actions

    # 9 - Clear the window
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw all window elements
    title.draw()
    input_caption.draw()
    input_field.draw()
    ok_button.draw()
    output_caption_1.draw()
    money_field_1.draw()
    output_caption_2.draw()
    money_field_2.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
