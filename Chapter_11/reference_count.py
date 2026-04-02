# reference_count.py

# Reference count example

class Square:

    def __init__(self, width: int, color: str):
        self.width: int = width
        self.color: str = color


# Instantiate an object
o_square_1: Square = Square(5, "red")
print(o_square_1)
# Reference count of the Square object is 1

# Now set another variable to the same object
o_square_2: Square = o_square_1
print(o_square_2)
# Reference count of the Square object is 2
