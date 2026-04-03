# slots_test.py

# Standard example that uses a dictionary
class Point:

    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

        print(x, y)

        # Try to create an additional instance variable
        self.color: str = "black"  # works fine

        print(self.color)


o_point: Point = Point(3, 5)


class PointWithSlots:
    #Define slots for only two instance variables
    __slots__ = ["x", "y"]

    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

        print(x, y)

        # Try to create an additional instance variable
        # Should fail
        self.color: str = "black"  # works fine

        print(self.color)


o_point_with_slots: PointWithSlots = PointWithSlots(3, 5)
