# fraction.py

# Fraction class
from __future__ import annotations
import math


class Fraction:

    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise TypeError(f"Numerator {numerator} must be an integer")

        if not isinstance(denominator, int):
            raise TypeError(f"Denominator {denominator} must be an integer")

        self.numerator: int = numerator
        self.denominator: int = denominator

        # Use the math package to find the greatest common divisor
        greatest_common_divisor: int = math.gcd(self.numerator, self.denominator)

        if greatest_common_divisor >  1:
            self.numerator //= greatest_common_divisor
            self.denominator //= greatest_common_divisor

        self.value: float = self.numerator / self.denominator

        # Normalize the sign of the numerator and denominator
        self.numerator: int = int(math.copysign(1.0, self.value)) * abs(self.numerator)
        self.denominator: int = abs(self.denominator)

    def get_value(self) -> float:
        return self.value

    def __str__(self) -> str:
        """Create a string representation of the fraction"""

        output: str = (f"    Fraction: {self.numerator}/{self.denominator}\n"
                       f"    Value: {self.value}")

        return output

    def __add__(self, o_other_fraction: "Fraction") -> Fraction:
        """ Add two fraction objects"""

        if not isinstance(o_other_fraction, Fraction):
            raise TypeError("Second value in attempt to add is not a Fraction")

        # Use the math package to find the least common multiple
        new_denominator: int = math.lcm(self.denominator, o_other_fraction.denominator)

        multiplication_factor: int = new_denominator // self.denominator
        equivalent_numerator: int = self.numerator * multiplication_factor

        other_multiplication_factor: int = new_denominator // o_other_fraction.denominator
        o_other_fraction_equivalent_numerator: int = o_other_fraction.numerator * other_multiplication_factor

        new_numerator: int = equivalent_numerator + o_other_fraction_equivalent_numerator

        o_added_fraction: Fraction = Fraction(new_numerator, new_denominator)

        return o_added_fraction

    def __eq__(self, o_other_fraction: "Fraction") -> bool:
        """ Test for equality"""

        if not isinstance(o_other_fraction, Fraction):
            return False    # not comparing to a fraction

        if (self.numerator == o_other_fraction.numerator) and (self.denominator == o_other_fraction.denominator):
            return True

        else:
            return False


# Test code
o_fraction_1: Fraction = Fraction(1, 3)     # create a Fraction object
o_fraction_2: Fraction = Fraction(2, 5)

print(f"Fraction 1\n{o_fraction_1}")  # print the object ... calls  __str__
print(f"Fraction 2\n{o_fraction_2}")

o_sum_fraction: Fraction = o_fraction_1 + o_fraction_2       # calls __add__
print(f"Sum is\n{o_sum_fraction}")

print(f"Are fractions 1 and 2 equal? {o_fraction_1 == o_fraction_2}")   # expect False
print()

o_fraction_3: Fraction = Fraction(-20, 80)
o_fraction_4: Fraction = Fraction(4, -16)

print(f"Fraction 3\n{o_fraction_3}")
print(f"Fraction 4\n{o_fraction_4}")

print(f"Are fractions 3 and 4 equal? {o_fraction_3 == o_fraction_4}")   # expect True
print()

o_fraction_5: Fraction = Fraction(5, 2)
o_fraction_6: Fraction = Fraction(500, 200)

print(f"Sum of 5/2 and 500/200\n{o_fraction_5 + o_fraction_6}")
