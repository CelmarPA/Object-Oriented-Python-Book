# pie_view.py

#  PieView - Roll The Dice

from pygame import Surface
from model import Model
import pygame
import pygame.gfxdraw
from math import radians, cos, sin
from pygwidgets import DisplayText
from constants import *

CENTER_X: int = 300
CENTER_Y: int = 300
RADIUS: int = 200
RADIUS_MINUS_1: int = RADIUS - 1
BLACK: tuple[int, int, int] = (0, 0, 0)


class PieView:
    n_rounds: int
    results_dict: dict[int, int]
    percents_dict: dict[int, int]

    def __init__(self, window: Surface, o_model: Model) -> None:
        self.window: Surface = window
        self.o_model: Model = o_model
        self.legend_field_dicts: dict[int, DisplayText] = {}
        y: int = 160

        # Create the legend fields
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            gray: tuple[int, int, int] = (index * 20, index * 20, index * 20)

            o_legend_field: DisplayText = DisplayText(window, (550, y), value=str(index), fontSize=32, textColor=gray)

            self.legend_field_dicts[index] = o_legend_field

            y += 25     # vertical spacing

    def update(self) -> None:
        n_rounds: int
        results_dict: dict[int, int]
        percents_dict: dict[int, int]

        n_rounds, results_dict, percents_dict = self.o_model.get_rounds_rolls_percents()

        self.n_rounds = n_rounds
        self.results_dict = results_dict
        self.percents_dict = percents_dict

        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            # Could use the count if we want to display it later
            # rollCount = resultsDict[index]
            percent: int = percents_dict[index]
            o_legend_field: DisplayText = self.legend_field_dicts[index]

            # Build percent as a string with one decimal digit
            percent: str = f"{percent:.1%}"
            o_legend_field.setValue(f"{index}:   {percent}")

    def draw_filled_arc(self, center_x: int, center_y: int, radius: int, degrees_1: float,
                        degrees_2: float, color: tuple[int, int, int]) -> None:
        """
        This method generates a list of points that are used to create
        a filled polygon representing an arc in the circle.  We'll use the
        angles passed in and a little trig to figure out the points in the arc
        """
        center_tuple: tuple[int, int] = (center_x, center_y)
        n_points_to_draw: int = int(degrees_2 - degrees_1)

        if n_points_to_draw == 0:
            return      # nothing to draw

        # Both degrees parameters need to be converted to radians for calculating points
        radians_1: float = radians(degrees_1)
        radians_2: float = radians(degrees_2)
        radians_diff: float = (radians_2 - radians_1) / n_points_to_draw

        # Start and end with the center point of the circle
        points_list: list[tuple[int | float, int | float]] = [center_tuple]

        # Determine the points on the edge of the arc
        for point_number in range(n_points_to_draw + 1):
            offset: float = point_number * radians_diff

            x: float = center_x + (radius * cos(radians_1 + offset))
            y: float = center_y + (radius * sin(radians_1 + offset))

            points_list.append((x, y))

        points_list.append(center_tuple)

        pygame.gfxdraw.filled_polygon(self.window, points_list, color)
        # If you would like black lines around each arc, uncomment the next line
        # pygame.gfxdraw.polygon(self.window, pointsList, BLACK)

    # Draw the slice of the pie (arc) for every roll total
    def draw(self) -> None:
        start_angle: float = 0.0

        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            percent: int = self.percents_dict[index]
            end_angle: float = start_angle + (percent * 360)
            gray: tuple[int, int, int] = (index * 20, index * 20, index * 20)

            self.draw_filled_arc(CENTER_X, CENTER_Y, RADIUS_MINUS_1, start_angle, end_angle, gray)

            self.legend_field_dicts[index].draw()

            start_angle = end_angle     # set up for next wedge

        pygame.draw.circle(self.window, BLACK, (CENTER_X, CENTER_Y), RADIUS, 2)
