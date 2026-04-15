# controller.py

#  Controller - Roll The Dice

from pygwidgets import TextButton, Image, TextRadioButton
from pyghelpers import textYesNoDialog
import sys
from bar_view import *
from pie_view import *
from text_view import *
from model import *
from input_number import *


BACKGROUND_COLOR: tuple[int, int, int] = (0, 222, 222)
N_ROUNDS_AT_START: int = 2500
LIGHT_GRAY: tuple[int, int, int] = (225, 225, 225)


class Controller:

    def __init__(self, window: Surface) -> None:
        self.window: Surface = window

        # Instantiate the Model
        self.o_model: Model = Model()

        # Instantiate different View objects
        self.o_bar_view: BarView = BarView(self.window, self.o_model)
        self.o_pie_view: PieView = PieView(self.window, self.o_model)
        self.o_text_view: TextView = TextView(self.window, self.o_model)

        # Default to bar view at start
        self.o_view = self.o_bar_view

        self.o_title_display: DisplayText = DisplayText(window, (250, 30), "Roll The Dice!",
                                                        fontName="monospace", fontSize=34, justified="center")

        self.o_quit_button: TextButton = TextButton(window, (20, 595), "Quit", width=100, height=35)

        self.o_rounds_display: DisplayText = DisplayText(window, (175, 604), "Number of rolls:",
                                                         fontName="monospace", fontSize=20, width=250, justified="right")

        self.o_rounds_input: InputNumber = InputNumber(window, (430, 600), value=str(N_ROUNDS_AT_START),
                                                       font_name="monospace", font_size=28, width=100,
                                                       initial_focus=True, keep_focus_on_submit=True,
                                                       allow_floating_number=False, allow_negative_number=False)

        self.o_roll_dice_button: TextButton = TextButton(window, (690, 595), "Roll Dice", width=100, height=35)

        self.o_dice_image: Image = Image(window, (650, 15), "images/twoDice.png")

        # This area reserved for the different views
        self.view_area: Rect = Rect(45, 70, WINDOW_WIDTH - 90, WINDOW_HEIGHT - 200)

        self.o_bar_button: TextRadioButton = TextRadioButton(window, (80, 540), "View", "Bar Chart",
                                                             value=True, fontSize=36)

        self.o_pie_button: TextRadioButton = TextRadioButton(window, (350, 540), "View", "Pie Chart",
                                                             fontSize=36)

        self.o_text_button: TextRadioButton = TextRadioButton(window, (620, 540), "View", "Text",
                                                              fontSize=36)


        # Generate the starting data, and tell the View about the results
        self.generate_new_data()
        self.o_view.update()

    def handle_event(self, event: Event) -> None:
        if self.o_quit_button.handleEvent(event):
            pygame.quit()
            sys.exit()

        if self.o_roll_dice_button.handleEvent(event) or self.o_rounds_input.handleEvent(event):
            self.generate_new_data()
            self.o_view.update()

        if self.o_bar_button.handleEvent(event):
            self.o_view = self.o_bar_view
            self.o_view.update()

        elif self.o_pie_button.handleEvent(event):
            self.o_view = self.o_pie_view
            self.o_view.update()

        elif self.o_text_button.handleEvent(event):
            self.o_view = self.o_text_view
            self.o_view.update()

    def generate_new_data(self) -> None:
        """
        This method gets the number of rolls from the input field and
        after checking for errors, tells the model to generate new data based
        on the number of rolls the user asked for.
        """

        try:
            n_rounds: int = self.o_rounds_input.getValue()

        except Exception as msg:
            textYesNoDialog(self.window, Rect(170, 180, 430, 170),
                            msg, "OK", None, backgroundColor=LIGHT_GRAY)

            return

        if n_rounds < 100:
            textYesNoDialog(self.window, Rect(170, 180, 430, 170),
                            "For meaningful results,\n enter 100 or more.", "OK",
                            None, backgroundColor=LIGHT_GRAY)

            return

        self.o_model.generate_rolls(n_rounds)

    def draw(self) -> None:
        # Draw everything the Controller is responsible for
        # (everything outside the black rectangle)
        self.window.fill(BACKGROUND_COLOR)

        self.o_bar_button.draw()
        self.o_pie_button.draw()
        self.o_text_button.draw()
        self.o_title_display.draw()
        self.o_dice_image.draw()
        self.o_rounds_display.draw()
        self.o_rounds_input.draw()
        self.o_roll_dice_button.draw()
        self.o_quit_button.draw()

        # Each view is responsible for drawing the element inside the black rectangle
        pygame.draw.rect(self.window, BLACK, self.view_area, 3)
        self.o_view.draw()      # tell the current view to draw itself
