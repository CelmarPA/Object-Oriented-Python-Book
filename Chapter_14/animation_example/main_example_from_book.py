# main_example_from_book.py

# Animation Example
# Shows examples of Animation and SpriteSheetAnimation objects

# 1 - Import packages
import pygame
import sys
from pygwidgets import Animation, SpriteSheetAnimation, DisplayText, TextButton, TextCheckBox


# 2 - Define constants
SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 480
FRAMES_PER_SECOND: int = 30
BG_COLOR: tuple[int, int, int] = (220, 220, 220)


# Define an example function to be used as a "callback"
def my_function(the_nickname: str| None) -> None:
    if the_nickname is None:
        print("In my_function, animation ended")

    else:
        print(f"In my_function, the animation with the nickname {the_nickname} ended")


# Define an example class with an example method to be used as a "callback"
class CallBackTest:

    @staticmethod
    def my_method(the_nickname: str | None) -> None:
        if the_nickname is None:
            print("In my_method, animation ended")

        else:
            print(f"In my_method, the animation named {the_nickname} ended")


# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.
dinosaur_anim_list: list[tuple[str, float]] = [
    ("images/Dinowalk/f1.png", .1),
    ("images/Dinowalk/f2.png", .1),
    ("images/Dinowalk/f3.png", .1),
    ("images/Dinowalk/f4.png", .1),
    ("images/Dinowalk/f5.png", .1),
    ("images/Dinowalk/f6.png", .1),
    ("images/Dinowalk/f7.png", .1),
    ("images/Dinowalk/f8.png", .1),
    ("images/Dinowalk/f9.png", .1),
    ("images/Dinowalk/f10.png", .1),
    ("images/Dinowalk/f11.png", .1),
    ("images/Dinowalk/f12.png", .1),
    ("images/Dinowalk/f13.png", .1),
    ("images/Dinowalk/f14.png", .1),
    ("images/Dinowalk/f15.png", .1),
    ("images/Dinowalk/f16.png", .1),
    ("images/Dinowalk/f17.png", .1)
]

# TRex
trex_animation_list: list[tuple[str, int]] = [
    ("images/TRex/f1.gif", .1),
    ("images/TRex/f2.gif", .1),
    ("images/TRex/f3.gif", .1),
    ("images/TRex/f4.gif", .1),
    ("images/TRex/f5.gif", .1),
    ("images/TRex/f6.gif", .1),
    ("images/TRex/f7.gif", .1),
    ("images/TRex/f8.gif", .1),
    ("images/TRex/f9.gif", .1),
    ("images/TRex/f10.gif", .1)
]

# 5 - Initialize variables
o_callback_test: CallBackTest = CallBackTest()   # instantiate a test object
o_title_text: DisplayText = DisplayText(window, (110, 80),
                                        "Animations                      SpriteSheetAnimations",
                                        fontSize=32)

o_dinosaur_animation: Animation = Animation(window, (22, 145), dinosaur_anim_list, autoStart=True, loop=False,
                                            callBack=my_function, nickname="Dinosaur")

o_play_button: TextButton = TextButton(window, (20, 240), "Play")
o_pause_button: TextButton = TextButton(window, (20, 280), "Pause")
o_stop_button: TextButton = TextButton(window, (20, 320), "Stop")
o_loop_checkbox: TextCheckBox = TextCheckBox(window, (20, 370), "Loop", value=False)
o_show_checkbox: TextCheckBox = TextCheckBox(window, (20, 400), "Show", value=True)

o_trex_animation: Animation = Animation(window, (180, 140), trex_animation_list, autoStart=False, loop=False,
                                        nIterations=3, callBack=o_callback_test.my_method)

o_instructions_text: DisplayText = DisplayText(window, (160, 320), "(Click image to activate)")

o_effect_animation: SpriteSheetAnimation = SpriteSheetAnimation(window, (400, 150), "images/effect_010.png",
                                                                35, 192, 192, .1,
                                                                autoStart=True, loop=True)

o_walk_animation: SpriteSheetAnimation = SpriteSheetAnimation(window, (460, 335), "images/male_walkcycle.png",
                                                              36, 64, 64,
                                                              (.1, .1, .1, .1, .1, .1, .1, .1, .3, .1,
                                                               .1, .1, .1, .1, .1, .1, .1, .3, .1, .1, .1, .1, .1, .1,
                                                               .1, .1, .3, .1, .1, .1, .1, .1, .1, .1, .1, .3),
                                                              autoStart=False, loop=False)

o_start_button: TextButton = TextButton(window, (440, 400), "Start")

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if o_play_button.handleEvent(event):
            o_dinosaur_animation.start()

        if o_pause_button.handleEvent(event):
            o_dinosaur_animation.pause()

        if o_stop_button.handleEvent(event):
            o_dinosaur_animation.stop()

        if o_loop_checkbox.handleEvent(event):
            current_loop_state: bool = o_dinosaur_animation.getLoop()
            o_dinosaur_animation.setLoop(not current_loop_state)

        if o_show_checkbox.handleEvent(event):
            show_state: bool = o_dinosaur_animation.getVisible()

            if show_state:
                o_dinosaur_animation.hide()

            else:
                o_dinosaur_animation.show()

        if o_start_button.handleEvent(event):
            o_walk_animation.start()

        if o_dinosaur_animation.handleEvent(event):
            o_dinosaur_animation.start()

        if o_trex_animation.handleEvent(event):
            o_trex_animation.start()

    # 8 - Do any "per frame" actions
    if o_trex_animation.update():
        print("In main code - TRex animation ended")

    if o_dinosaur_animation.update():
        print("In main code - Dinosaur animation ended")

    if o_effect_animation.update():
        print("In main code - Effect animation ended")

    if o_walk_animation.update():
        print("In main code - Walk animation ended")

    # 9 - Clear the screen
    window.fill(BG_COLOR)

    # 10 - Draw all screen elements
    o_title_text.draw()
    o_dinosaur_animation.draw()
    o_play_button.draw()
    o_pause_button.draw()
    o_stop_button.draw()
    o_loop_checkbox.draw()
    o_show_checkbox.draw()
    o_trex_animation.draw()
    o_instructions_text.draw()
    o_effect_animation.draw()
    o_walk_animation.draw()
    o_start_button.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
