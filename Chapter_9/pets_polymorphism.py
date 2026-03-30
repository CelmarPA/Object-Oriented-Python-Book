# pets_polymorphism.py

# Pets polymorphism
# Three classes, all with a different "speak" method

class Dog:

    def __init__(self, name: str):
        self.name: str = name

    def speak(self):
        print(f"{self.name} says bark, bark, bark!")


class Cat:

    def __init__(self, name: str):
        self.name: str = name

    def speak(self):
        print(f"{self.name} says meeeoooow")


class Bird:

    def __init__(self, name: str):
        self.name: str = name

    def speak(self):
        print(f"{self.name} says tweet")


o_dog_1: Dog = Dog("Rover")
o_dog_2: Dog = Dog("Fido")
o_cat_1: Cat = Cat("Fluffy")
o_cat_2: Cat = Cat("Spike")
o_bird: Bird = Bird("Big Bird")

pets_list: list = [o_dog_1, o_dog_2, o_cat_1, o_cat_2, o_bird]

# Send the same message (call the same method) of all pets
for o_pet in pets_list:
    o_pet.speak()
