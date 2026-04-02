# delete_example_teacher_student.py

# Student class
class Student:

    def __init__(self, name: str) -> None:
        self.name: str = name
        print(f"Creating Student object {self.name}")

    def __del__(self):
        print(f"In the __del__ method for student: {self.name}")


# Teacher class
class Teacher:

    def __init__(self):
        print(f"Creating the Teacher object")
        self.o_student_1: Student = Student("Joe")
        self.o_student_2: Student = Student("Sue")
        self.o_student_3: Student = Student("Chris")

    def __del__(self):
        print(f"In the __del__ method for Teacher")


# Instantiate the Teacher object (that creates Student objects)
o_teacher: Teacher = Teacher()

# Delete the Teacher object
del o_teacher
