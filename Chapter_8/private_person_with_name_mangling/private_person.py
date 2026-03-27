# private_person.py

# PrivatePerson class

class PrivatePerson:

    def __init__(self, name: str, private_date: str):
        self.name: str = name
        self.__private_data: str = private_date

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name: str = name
