# oo_tv_two_instances.py

# Two TV objects with calls to their methods
class TV:

    def __init__(self, brand: str, location: str) -> None:
        self.brand: str = brand
        self.location: str = location
        self.is_on: bool = False
        self.is_muted: bool = False
        # Some default list of channels
        self.channel_list: list = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.n_channel: int = len(self.channel_list)
        self.channel_index: int = 0
        self.VOLUME_MINIMUM: int = 0    # constant
        self.VOLUME_MAXIMUM: int = 10    # constant
        self.volume: int = self.VOLUME_MAXIMUM // 2    # integer divide

    def power(self) -> None:
        self.is_on = not self.is_on    # toggle

    def volume_up(self) -> None:
        if not self.is_on:
            return

        if self.is_muted:
            self.is_muted = False   # changing the volume while muted unmutes the sound

        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volume_down(self) -> None:
        if not self.is_on:
            return

        if self.is_muted:
            self.is_muted = False  # changing the volume while muted unmutes the sound

        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1

    def channel_up(self) -> None:
        if not self.is_on:
            return

        self.channel_index += 1

        if self.channel_index > self.n_channel:
            self.channel_index = 0    # wrap around to the first channel

    def channel_down(self) -> None:
        if not self.is_on:
            return

        self.channel_index -= 1

        if self.channel_index < 0:
            self.channel_index = self.n_channel - 1    # wrap around to the top channel

    def mute(self) -> None:
        if not self.is_on:
            return

        self.is_muted = not self.is_muted

    def set_channel(self, new_channel: int) -> None:
        if new_channel in self.channel_list:
            self.channel_index = self.channel_list.index(new_channel)

        # if the newChannel is not in our list of channels, don't do anything

    def show_info(self) -> None:
        print()
        print(f"Status of TV: {self.brand}")
        print(f"    Location: {self.location}")
        if self.is_on:
            print(f"    TV is: On")
            print(f"    Channel is: {self.channel_list[self.channel_index]}")

            if self.is_muted:
                print(f"    Volume is: {self.volume}, (sound is muted)")

            else:
                print(f"    Volume is: {self.volume}")

        else:
            print("    TV is: Off")


# Main code
o_TV_1 = TV("Samsung", "Family room")    # create one TV object
o_TV_2 = TV("Sony", "Bedroom")    # create another TV object

# Turn both TVs on
o_TV_1.power()
o_TV_2.power()

# Raise the volume of TV1
o_TV_1.volume_up()
o_TV_1.volume_up()

# Raise the volume of TV2
o_TV_2.volume_up()
o_TV_2.volume_up()
o_TV_2.volume_up()
o_TV_2.volume_up()
o_TV_2.volume_up()

# Change TV2's channel, then mute it
o_TV_2.set_channel(44)
o_TV_2.mute()

# Now display both TVs
o_TV_1.show_info()
o_TV_2.show_info()
