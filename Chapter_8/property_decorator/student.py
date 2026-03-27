# student.py

# Using a property to (indirectly) access data in an object

class Student:

    def __init__(self, name: str, starting_grade: int = 0):
        self.__name: str = name
        self.grade: int = starting_grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, new_grade: str) -> None:
        try:
            new_grade: int = int(new_grade)

        except (TypeError, ValueError) as e:
            raise type(e) (f"New grade: {new_grade} is an invalid type.")

        if (new_grade < 0) or (new_grade > 100):
            raise ValueError(f"New grade: {new_grade} must be between 0 and 100.")

        self.__grade: int = new_grade
