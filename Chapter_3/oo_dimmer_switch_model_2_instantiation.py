# oo_dimmer_switch_model_2_instantiation.py

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


# Create three DimmerSwitch objects
o_dimmer_1 = DimmerSwitch("Dimmer1")
print(type(o_dimmer_1))
print(o_dimmer_1)
print()

o_dimmer_2 = DimmerSwitch("Dimmer2")
print(type(o_dimmer_2))
print(o_dimmer_2)
print()

o_dimmer_3 = DimmerSwitch("Dimmer3")
print(type(o_dimmer_3))
print(o_dimmer_3)
print()

print(f"o_dimmer_1 variables: {vars(o_dimmer_1)}")