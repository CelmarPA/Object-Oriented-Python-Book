# oo_light_switch_with_test_code.py

class LightSwitch:

    def __init__(self) -> None:
        self.switch_is_on = False

    def turn_on(self) -> None:
        # turn the light on
        self.switch_is_on = True

    def turn_off(self) -> None:
        # turn the light off
        self.switch_is_on = False

    def show(self) -> None:  # added for testing
        print(self.switch_is_on)


# Main code
o_light_switch = LightSwitch() # create a LightSwitch object

# Calls to methods
o_light_switch.show()
o_light_switch.turn_on()
o_light_switch.show()
o_light_switch.turn_off()
o_light_switch.show()
o_light_switch.turn_on()
o_light_switch.show()
