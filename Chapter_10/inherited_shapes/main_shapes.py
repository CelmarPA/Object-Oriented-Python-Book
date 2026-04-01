# main_shapes.py

# Main Shapes program

import sys
from pygame.locals import *
from square import *
from circle import *
from triangle import *
import pygwidgets


# set up the constants
WHITE: tuple[int] = (255, 255, 255)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30
N_SHAPES: int = 10

# set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

shapes_list: list = []
shapes_classes_tuple: tuple = (Square, Circle, Triangle)

for i in range(N_SHAPES):
    randomly_chosen_class: type = random.choice(shapes_classes_tuple)
    o_shape = randomly_chosen_class(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    shapes_list.append(o_shape)

o_status_line: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (4, 4), "Click on shapes", fontSize=28)

# Main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            # Reverse order to check last drawn shape first
            for o_shape in shapes_list:
                if o_shape.clicked_inside(event.pos):
                    area = o_shape.get_area()
                    area: str = str(area)
                    the_type: str = o_shape.get_type()
                    new_text: str = f"Clicked on a {the_type} whose area is {area}"
                    o_status_line.setValue(new_text)
                    break # only deal with topmost shape

        window.fill(WHITE)

        for o_shape in shapes_list:
            o_shape.draw()

        o_status_line.draw()

        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)
