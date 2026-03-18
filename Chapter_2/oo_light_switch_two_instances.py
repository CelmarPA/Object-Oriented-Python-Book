# oo_light_switch_two_instances.py

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
o_light_switch_1 = LightSwitch() # create a LightSwitch object
o_light_switch_2 = LightSwitch() # create another LightSwitch object

# Test code
o_light_switch_1.show()
o_light_switch_2.show()
o_light_switch_1.turn_on() # Turn switch 1 on

# Switch 2 should be off at start, but this makes it clearer
o_light_switch_2.turn_off()
o_light_switch_1.show()
o_light_switch_2.show()
