# main_vectors.py

# Vector test code

from vector import *


v1: Vector = Vector(3, 4)
v2: Vector = Vector(2, 2)
v3: Vector = Vector(3, 4)

# These lines print Boolean or numeric values
print(v1 == v2)
print(v1 == v3)
print(v1 < v2)
print(v1 > v2)
print(abs(v1))
print(abs(v2))
print()

# These lines print Vectors (calls the __str__() method)
print('Vector 1:', v1)
print('Vector 2:', v2)
print('Vector 1 + Vector 2:', v1 + v2)
print('Vector 1 - Vector 2:', v1 - v2)
print('Vector 1 times Vector 2:', v1 * v2)
print('Vector 2 times 5:', v1 * 5)
