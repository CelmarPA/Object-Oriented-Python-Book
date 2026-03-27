# main_person_getter_setter.py

# Person example main program using getters and setters

from person import *


o_person_1: Person = Person("Jose Schmoe", 90000)
o_person_2: Person = Person("Jane Smith", 99000)

# Get the salaries using getter and print
print(o_person_1.get_salary())
print(o_person_2.get_salary())

# Change the salaries using setter
o_person_1.set_salary(100000)
o_person_2.set_salary(111111)

# Get the salaries and print again
print(o_person_1.get_salary())
print(o_person_2.get_salary())
