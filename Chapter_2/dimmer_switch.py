# dimmer_switch.py

# DimmerSwitch class
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
    def show(self):
        print(f"Switch is on? {self.switch_is_on}")
        print(f"Brightness is: {self.brightness}")
