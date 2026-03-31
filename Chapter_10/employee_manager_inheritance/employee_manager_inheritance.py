# employee_manager_inheritance.py

# Employee Manager inheritance
#
# Define the Employee class, which we will use as a base class

class Employee:

    def __init__(self, name: str, title: str, rate_per_hour: str | None = None):
        self.name: str = name
        self.title: str = title

        if rate_per_hour is not None:
            rate_per_hour: float = float(rate_per_hour)

        self.rate_per_hour: float = rate_per_hour

    def get_name(self) -> str:
        return self.name

    def get_title(self) -> str:
        return self.title

    def pay_per_year(self) -> float:
        # 52 weeks * 5 days a week * 8 hours per day
        pay: float = 52 * 5 * 8 * self.rate_per_hour

        return pay


# Define a Manager subclass that inherits from Employee
class Manager(Employee):

    def __init__(self, name: str, title: str, salary: str, reports_list: list[Employee] | None = None):

        self.salary: float = float(salary)

        if reports_list is None:
            reports_list: list = []

        self.reports_list: list = reports_list

        super().__init__(name, title)

    def get_reports(self) -> list[Employee]:
        return self.reports_list

    def pay_per_year(self, give_bonus: bool = False) -> float:
        pay: float = self.salary

        if give_bonus:
            pay += (.10 * self.salary)

            print(f"{self.name} gets a bonus for good work")

        return pay


# Create objects
o_employee_1: Employee = Employee("Joe Schmoe", "Pizza Maker", 16)
o_employee_2: Employee = Employee("Chris Smith", "Cashier", 14)

o_manager: Manager = Manager("Sue Jones", "Pizza Restaurant Manager",
                             55000, [o_employee_1, o_employee_2])

# Call methods of the Employee objects
print(f"Employee name: {o_employee_1.get_name()}")
print(f"Employee salary: ${o_employee_1.pay_per_year():,.2f}")
print(f"Employee name: {o_employee_2.get_name()}")
print(f"Employee salary: ${o_employee_2.pay_per_year():,.2f}")
print()

# Call methods of the Manager object
manager_name: str = o_manager.get_name()
print(f"Manager name: {manager_name}")

# Give the manager a bonus
print(f"Manager salary: ${o_manager.pay_per_year(True):,.2f}")
print(f"{manager_name} ({o_manager.get_title()}) direct reports:")
reports_list: list[Employee] = o_manager.get_reports()

for o_employee in reports_list:
    print(f"    {o_employee.get_name()} ({o_employee.get_title()})")
