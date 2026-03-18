# 00_dimmer_switch_with_test_code.py

# DimmerSwitch class with test code
class DimmerSwitch:

    def __init__(self) -> None:
        self.switch_is_on: bool = False
        self.brightness: int = 0

    def turn_on(self) -> None:
        self.switch_is_on = True

    def turn_off(self) -> None:
        self.switch_is_on = False

    def raise_level(self) -> None:
        if self.brightness < 10:
            self.brightness += 1

    def lower_level(self) -> None:
        if self.brightness > 0:
            self.brightness -= 1

    # Extra method for debugging
    def show(self) -> None:
        print(f"Switch is on? {self.switch_is_on}")
        print(f"Brightness is: {self.brightness}")


# Main code
o_dimmer = DimmerSwitch()

# Turn switch on, and raise the level 5 times
o_dimmer.turn_on()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.show()

# Lower the level 2 times, and turn switch off
o_dimmer.lower_level()
o_dimmer.lower_level()
o_dimmer.turn_off()
o_dimmer.show()

# Turn switch on, and raise the level 3 times
o_dimmer.turn_on()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.show()