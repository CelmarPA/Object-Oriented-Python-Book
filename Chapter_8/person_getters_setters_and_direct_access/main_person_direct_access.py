# main_person_direct_access.py

# Person example main program using direct access

from person import *

o_person_1: Person = Person("Joe Schmoe", 90000)
o_person_2: Person = Person("Jane Smith", 99000)

# Get the values of the salary variable directly
print(o_person_1.salary)
print(o_person_2.salary)

# Change the salary variable directly
o_person_1.salary = 100000
o_person_2.salary = 111111

# Get the updated salaries and print again
print(o_person_1.salary)
print(o_person_2.salary)
