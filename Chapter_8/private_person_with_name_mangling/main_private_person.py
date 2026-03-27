# PrivatePerson Example main program

from private_person import *


o_private_person_1: PrivatePerson = PrivatePerson("Joe Schmoe", "Data for Joe Schmoe")
o_private_person_2: PrivatePerson = PrivatePerson("Jane Smith", "Data for Jane Smith")

# Using getter and setter - works fine
print(o_private_person_1.get_name())

o_private_person_1.set_name('Joseph Schmoe')
print(o_private_person_1.get_name())

# Attempted use of direct access would fail
# print(o_private_person_1.__private_data)

# Using mangled name - works
print(o_private_person_1._PrivatePerson__private_data)
o_private_person_1._PrivatePerson__private_data = "Modified data for Joeseph Schmoe"
print(o_private_person_1._PrivatePerson__private_data)
