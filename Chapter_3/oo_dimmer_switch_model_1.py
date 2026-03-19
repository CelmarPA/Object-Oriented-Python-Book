# oo_dimmer_switch_model_1.py

# Dimmer Switch class

class DimmerSwitch:

    def __init__(self, label: str) -> None:
        self.label: str = label
        self.switch_is_on: bool = False
        self.brightness: int = 0

    def turn_on(self) -> None:
        self.switch_is_on = True
        # turn the light on at self.brightness

    def turn_off(self) -> None:
        self.switch_is_on = False
        # turn the light off

    def raise_level(self) -> None:
        if self.brightness < 10:
            self.brightness += 1

    def lower_level(self) -> None:
        if self.brightness > 0:
            self.brightness -= 1

    # Extra method for debugging
    def show(self):
        print(f"Label: {self.label}")
        print(f"Switch is on? {self.switch_is_on}")
        print(f"Brightness is: {self.brightness}")
        print()

# Create first DimmerSwitch, turn it on, and raise the level twice
o_dimmer_1 = DimmerSwitch("Dimmer1")
o_dimmer_1.turn_on()
o_dimmer_1.raise_level()
o_dimmer_1.raise_level()

# Create second DimmerSwitch, turn it on, and raise the level 3 times
o_dimmer_2 = DimmerSwitch("Dimmer2")
o_dimmer_2.turn_on()
o_dimmer_2.raise_level()
o_dimmer_2.raise_level()
o_dimmer_2.raise_level()

# Create third DimmerSwitch, using the default settings
o_dimmer_3 = DimmerSwitch("Dimmer3")

# Ask each switch to show itself
o_dimmer_1.show()
o_dimmer_2.show()
o_dimmer_3.show()



















