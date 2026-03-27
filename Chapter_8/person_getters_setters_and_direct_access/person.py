# person.py

class Person:

    def __init__(self, name: str, salary: int):
        self.name: str = name
        self.salary: int = salary

    # Allow the caller to retrieve the salary
    def get_salary(self):
        return self.salary

    # Allow the caller to set a new salary
    def set_salary(self, salary: int):
        self.salary: int = salary
