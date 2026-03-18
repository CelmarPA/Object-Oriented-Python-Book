# oo_light_switch.py

class LightSwitch:

    def __init__(self) -> None:
        self.switch_is_on = False

    def turn_on(self) -> None:
        # turn the light on
        self.switch_is_on = True

    def turn_off(self) -> None:
        # turn the light off
        self.switch_is_on = False
