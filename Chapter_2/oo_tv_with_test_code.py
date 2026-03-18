# oo_tv_with_test_code.py

# TV class with test code
class TV:

    def __init__(self) -> None:
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
        print("TV Status:")
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
o_TV = TV()    # create the TV object

# Turn the TV on and show the status
o_TV.power()
o_TV.show_info()

# Change the channel up twice, raise the volume twice, show status
o_TV.channel_up()
o_TV.channel_up()
o_TV.volume_up()
o_TV.volume_up()
o_TV.show_info()

# Turn the TV off, show status, turn the TV on, show status
o_TV.power()
o_TV.show_info()
o_TV.power()
o_TV.show_info()

# Lower the volume, mute the sound, show status
o_TV.volume_down()
o_TV.mute()
o_TV.show_info()

# Change the channel to 11, mute the sound, show status
o_TV.set_channel(11)
o_TV.mute()
o_TV.show_info()
