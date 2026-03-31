# vector.py

# Vector class
from __future__ import annotations
import math


class Vector:

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y:int = y

    def __add__(self,  o_other: "Vector") -> "Vector":      # called for + operator
        if not isinstance(o_other, Vector):
            raise TypeError("Second object must be a Vector")

        return Vector(self.x + o_other.x, self.y + o_other.y)

    def __sub__(self, o_other: "Vector") -> Vector:         # called for - operator
        if not isinstance(o_other, Vector):
            raise TypeError("Second object must be a Vector")

        return Vector(self.x - o_other.x, self.y - o_other.y)

    def __mul__(self, o_other: "Vector | float | int") -> Vector:         # called for * operator
        # Special code to allow for multiplying by a vector or a scalar
        if isinstance(o_other, Vector):    # multiply two vectors
            return Vector((self.x * o_other.x), (self.y * o_other.y))

        elif isinstance(o_other, (int, float)):    # multiply by a scalar
            return Vector((self.x * o_other), (self.y * o_other))

        else:
            raise TypeError("Second value must be a vector or scalar")

    def __abs__(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __eq__(self, o_other: "Vector") -> bool:    # called for == operator
        if not isinstance(o_other, Vector):
            raise TypeError("Second object must be a Vector")

        return (self.x == o_other.x) and (self.y == o_other.y)

    def __ne__(self, o_other: "Vector") -> bool:    # called for != operator
        if not isinstance(o_other, Vector):
            raise TypeError("Second object must be a Vector")

        return not (self == o_other)    # calls __eq__

    def __lt__(self, o_other: "Vector") -> bool:
        if not isinstance(o_other, Vector):
            raise TypeError("Second object must be a Vector")

        if abs(self) < abs(o_other):    # calls __abs__ method
            return True

        else:
            return False

    def __gt__(self, o_other: "Vector") -> bool:
        if not isinstance(o_other, Vector):
            raise TypeError("Second object must be a Vector")

        if abs(self) > abs(o_other):    # calls __abs__ method
            return True

        else:
            return False

    def __str__(self):
        return f"This vector has the value ({self.x}, {self.y})"
