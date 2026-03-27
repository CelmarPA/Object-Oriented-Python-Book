# main_property.py

from student import *

# Main Student property example
o_student_1: Student = Student("Joe Schmoe")
o_student_2: Student = Student("Jane Smith")

# Get the students' grades using the 'grade' property and print
print(o_student_1.grade)
print(o_student_2.grade)
print()

# Set new values using the 'grade' property
o_student_1.grade = 85
o_student_2.grade = 92

print(o_student_1.grade)
print(o_student_2.grade)
