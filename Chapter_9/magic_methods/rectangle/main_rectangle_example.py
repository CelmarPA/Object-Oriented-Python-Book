# main_rectangle_example.py

import sys
from pygame.locals import *
from rectangle import *


# Set up the constants
WHITE: tuple[int] = (255, 255, 255)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30
N_RECTANGLES: int = 10
FIRST_RECTANGLE: str = "first"
SECOND_RECTANGLE: str = "second"

# Set up the window
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock: pygame.time.Clock = pygame.time.Clock()

rectangles_list: list[Rectangle] = []

for i in range(N_RECTANGLES):
    o_rectangle: Rectangle = Rectangle(window)
    rectangles_list.append(o_rectangle)

o_first_rectangle: Rectangle | None = None
o_second_rectangle: Rectangle | None = None
witch_rectangle: str = FIRST_RECTANGLE

# Main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for o_rectangle in rectangles_list:
                if o_rectangle.clicked_inside(event.pos):
                    print(f"Clicked on {witch_rectangle} rectangle.")

                    if witch_rectangle == FIRST_RECTANGLE:
                        o_first_rectangle: Rectangle = o_rectangle
                        witch_rectangle: str = SECOND_RECTANGLE

                    elif witch_rectangle == SECOND_RECTANGLE:
                        o_second_rectangle: Rectangle = o_rectangle
                        # User has chosen 2 rectangles, let's compare

                        if o_first_rectangle == o_second_rectangle:
                            print("Rectangles are the same size.")

                        elif o_first_rectangle < o_second_rectangle:
                            print("First rectangle is smaller than second rectangle.")

                        else: # must be larger
                            print("First rectangle is larger than second rectangle.")

                        witch_rectangle = FIRST_RECTANGLE

    # Clear the window and draw all rectangles
    window.fill(WHITE)

    for o_rectangle in rectangles_list:
        o_rectangle.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
