# main_test_pygwidgets.py

# Demo of pygwidgets capabilities

# 1 - Import libraries
import pygame
from pygame.locals import *
import pygwidgets
import os
import sys

# The next line is here just in case you are running from the command line
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 2 - Define constants
BLACK: tuple[int] = (0, 0, 0)
BLACKISH: tuple[int] = (10, 10, 10)
GRAY: tuple[int] = (128, 128, 128)
WHITE: tuple[int] = (255, 255, 255)
BACKGROUND_COLOR: tuple[int] = (0, 180, 180)
WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 640
FRAMES_PER_SECOND: int = 30

# The function and Test class and method below are not required.
# These are only here as a demonstration of how you could use a callback approach to handling events if you want to.

# Define a function to be used as a "callBack"
def my_function(the_nickname):
    if the_nickname is None:
        print("In my_function, a button was clicked")

    else:
        print(f"In my_function,the button name, {the_nickname} was clicked")


# Define a class with a method to be used as a "callback"
class Test:

    def __init__(self):

        pass

    def my_method(self, the_nickname):
        if the_nickname is None:
            print("In my_method, a button was clicked")

        else:
            print(f"In my_method, the button named {the_nickname} was clicked")

# 3 - Initialize the world
pygame.init()
window: pygame.Surface = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock: pygame.time.Clock = pygame.time.Clock()      # create a clock object

o_test: Test = Test()


# 4 - Load assets: image(s), sounds,  etc.
o_background_image: pygwidgets.Image = pygwidgets.Image(window, (0, 0), "images/background.jpg")

o_display_text_title: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (0, 20), "pygwidgets example by Irv Kalb",
                                                                      fontSize=36, width=640, textColor=BLACK, justified='center')

o_input_text_a: pygwidgets.InputText = pygwidgets.InputText(window, (20, 100), "Default input text",
                                                            textColor=WHITE, backgroundColor=BLACK,
                                                            fontSize=24, width=250)

o_input_text_b: pygwidgets.InputText = pygwidgets.InputText(window, (20, 200), initialFocus=True,
                                                            textColor=(0, 0, 255),
                                                            fontSize=28)    # add: , mask='*' for passwords

o_display_text_a: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (20, 300), "Here is some display text",
                                                                  fontSize=24, textColor=WHITE, justified="center")

o_display_text_b: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (20, 400), "Here is some display text",
                                                                  fontSize=24, textColor=BLACK, backgroundColor=WHITE)

o_restart_button: pygwidgets.CustomButton = pygwidgets.CustomButton(window, (100, 430),
                                                                    "images/restartButtonUp.png",
                                                                    down='images/restartButtonDown.png',
                                                                    over='images/restartButtonOver.png',
                                                                    disabled='images/restartButtonDisabled.png',
                                                                    soundOnClick='sounds/blip.wav',
                                                                    nickname='restartButton',
                                                                    callBack=my_function)  # callBack here is not required

# o_check_box_a controls the availability the custom radio buttons
# o_check_box_b controls the availability of the text radio buttons
o_check_box_a: pygwidgets.CustomCheckBox = pygwidgets.CustomCheckBox(window, (450, 110),value=True,
                                                                 on='images/checkBoxOn.png',
                                                                 off='images/checkBoxOff.png',
                                                                 onDown='images/checkBoxOnDown.png',
                                                                 offDown='images/checkBoxOffDown.png',
                                                                 onDisabled='images/checkBoxOnDisabled.png',
                                                                 offDisabled='images/checkBoxOffDisabled.png')


o_radio_custom_1: pygwidgets.CustomRadioButton = pygwidgets.CustomRadioButton(window, (500, 150), 'Custom Group',
                                            on='images/radioLowOn.png', off='images/radioLowOff.png',
                                            onDown='images/radioLowOnDown.png', offDown='images/radioLowOffDown.png',
                                            onDisabled='images/radioLowOnDisabled.png', offDisabled='images/radioLowOffDisabled.png',
                                            value=True, nickname='Low')

o_radio_custom_2: pygwidgets.CustomRadioButton = pygwidgets.CustomRadioButton(window, (500, 190), 'Custom Group',
                                            on='images/radioMedOn.png', off='images/radioMedOff.png',
                                            onDown='images/radioMedOnDown.png', offDown='images/radioMedOffDown.png',
                                            onDisabled='images/radioMedOnDisabled.png', offDisabled='images/radioMedOffDisabled.png',
                                            value=False, nickname='Med')

o_radio_custom_3: pygwidgets.CustomRadioButton = pygwidgets.CustomRadioButton(window, (500, 230), 'Custom Group',
                                            on='images/radioHighOn.png', off='images/radioHighOff.png',
                                            onDown='images/radioHighOnDown.png', offDown='images/radioHighOffDown.png',
                                            onDisabled='images/radioHighOnDisabled.png', offDisabled='images/radioHighOffDisabled.png',
                                            value=False, nickname='High')

o_check_box_b: pygwidgets.TextCheckBox = pygwidgets.TextCheckBox(window, (450, 295), "Allow Radio Buttons")

o_radio_text_1: pygwidgets.TextRadioButton = pygwidgets.TextRadioButton(window, (500, 320), 'Default Group',
                                                                        'Radio Text 1', value=False)

o_radio_text_2: pygwidgets.TextRadioButton = pygwidgets.TextRadioButton(window, (500, 360), 'Default Group',
                                                                        'Radio Text 2', value=False)

o_radio_text_3: pygwidgets.TextRadioButton = pygwidgets.TextRadioButton(window, (500, 400), 'Default Group',
                                                                        'Radio Text 3', value=False)

o_status_button: pygwidgets.TextButton = pygwidgets.TextButton(window, (500, 430), "Show Status",
                                                               callBack=o_test.my_method)   # callBack here is not required

o_dragger: pygwidgets.Dragger = pygwidgets.Dragger(window, (300, 200),
                                                   'images/dragMeUp.png',
                                                   'images/dragMeDown.png',
                                                   'images/dragMeOver.png',
                                                   'images/dragMeDisabled.png',
                                                   nickname='My Dragger')

o_python_icon: pygwidgets.Image = pygwidgets.Image(window, (15, 500), "images/pythonIcon.png")

o_image_collection: pygwidgets.ImageCollection = pygwidgets.ImageCollection(window, (400, 490),
                                                                            {'start': 'imageStart.jpg',
                                                                             'left': 'imageLeft.jpg',
                                                                             'right': 'imageRight.jpg',
                                                                             'up': 'imageUp.jpg',
                                                                             'down': 'imageDown.jpg'},
                                                                            'start', path='images/')

o_image_instructions: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (400, 595), "Click then type l, r, d, u, s, or Space")

o_icon_instructions: pygwidgets.DisplayText = pygwidgets.DisplayText(window, (15, 595),
                                                                     "Click then up or down arrow to resize,\n" +
                                                                     "left or right arrow to rotate, \n" +
                                                                     "h or v to flip horizontal or vertical")

o_frisbee_image: pygwidgets.Image = pygwidgets.Image(window, (562, 2), "images/frisbee.png")

# 5 - Initialize variables
counter: int = 0
angle: int = 0
pct: int = 100

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # check if the event is the close button
        if event.type == pygame.QUIT:
            # if it is quit, the program
            pygame.quit()
            sys.exit()

        if o_input_text_a.handleEvent(event):   # pressed Return or Enter
            the_text: str = o_input_text_a.getValue()
            print(f"The text of o_input_text_a is: {the_text}")

        if o_input_text_b.handleEvent(event):   # pressed Return or Enter
            the_text: str = o_input_text_b.getValue()
            print(f"The text of o_input_text_b is: {the_text}")

        if o_restart_button.handleEvent(event):  # clicked
            counter: int = 0
            print(f"Content of first input text is: {o_input_text_a.getValue()}")
            print(f"Content of second input text is: {o_input_text_b.getValue()}")

        if o_check_box_a.handleEvent(event):  # toggled
            a_on: bool = o_check_box_a.getValue()
            print(f"o_check_box_a was clicked, new value is: {a_on}")

            if a_on:
                o_radio_custom_1.enable()
                o_radio_custom_2.enable()
                o_radio_custom_3.enable()

            else:
                o_radio_custom_1.disable()
                o_radio_custom_2.disable()
                o_radio_custom_3.disable()

        if o_radio_custom_1.handleEvent(event):  # selected
            print("Radio button custom1 was clicked")

        if o_radio_custom_2.handleEvent(event):  # selected
            print("Radio button custom2 was clicked")

        if o_radio_custom_3.handleEvent(event):  # selected
            print("Radio button custom3 was clicked")

        if o_check_box_b.handleEvent(event):  # toggled
            b_on: bool = o_check_box_b.getValue()
            print(f"o_check_box_b was clicked, new value is: {b_on}")

            if b_on:
                o_radio_text_1.enableGroup()    # enable all radio buttons in group that contains this radio button
                # could alternatively have used (does the same as):
                # o_radio_custom_1.enable()
                # o_radio_custom_2.enable()
                # o_radio_custom_3.enable()

            else:
                o_radio_text_1.disableGroup()   # disable all buttons in this group
                # could alternatively have used (does the same as):
                # o_radio_custom_1.disable()
                # o_radio_custom_2.disable()
                # o_radio_custom_3.disable()

        if o_radio_text_1.handleEvent(event):  # selected
            print("Radio button text1 was clicked")

        if o_radio_text_2.handleEvent(event):  # selected
            print("Radio button text2 was clicked")

        if o_radio_text_3.handleEvent(event):  # selected
            print("Radio button text3 was clicked")

        if o_status_button.handleEvent(event):   # clicked
            nickname: str = o_radio_custom_1.getSelectedRadioButton()
            print(f"The currently selected custom Radio Button is: {nickname}")

            nickname: str = o_radio_text_1.getSelectedRadioButton()
            print(f"The currently selected Text Radio Button is: {nickname}")

        if o_dragger.handleEvent(event):
            print(f"Done dragging, dragger nickname was: {o_dragger.getNickname()}")
            print(f"  Mouse up at: {o_dragger.getMouseUpLoc()}")
            print(f"  Dragger is now located at: {o_dragger.getLoc()}")

        if o_python_icon.handleEvent(event):
            print("Got click on the Python icon")

        if o_image_collection.handleEvent(event):
            print("Got click on image collection")

        if o_frisbee_image.handleEvent(event):
            print("Got click on the frisbee image")


        if event.type == pygame.KEYDOWN:
            if o_python_icon.getFocus():
                if event.key == pygame.K_h:
                    o_python_icon.flipHorizontal()

                elif event.key == pygame.K_v:
                    o_python_icon.flipVertical()

            if o_image_collection.getFocus():
                if event.key == pygame.K_l:
                    o_image_collection.replace("left")

                elif event.key == pygame.K_r:
                    o_image_collection.replace('right')

                elif event.key == pygame.K_u:
                    o_image_collection.replace('up')

                elif event.key == pygame.K_d:
                    o_image_collection.replace('down')

                elif event.key == pygame.K_s:
                    o_image_collection.replace('start')

                elif event.key == pygame.K_SPACE:
                    o_image_collection.replace('')

    key_pressed_list: list = pygame.key.get_pressed()

    if key_pressed_list[pygame.K_LEFT]:
        o_python_icon.rotate(-5)

    if key_pressed_list[pygame.K_RIGHT]:
        o_python_icon.rotate(5)

        # If we wanted to keep track of the angle, we could start with:  angle = 0
        # Then for every left arrow:  angle = angle + 5
        # and for every right arrow:  angle = angle - 5
        # Finally, call:  oPythonIcon.rotateTo

    if key_pressed_list[pygame.K_UP]:
        scaleFromCenter = not (key_pressed_list[pygame.K_LSHIFT] or key_pressed_list[pygame.K_RSHIFT])
        pct = pct + 10
        o_python_icon.scale(pct, scaleFromCenter=scaleFromCenter)
        # print('Scaling up to', pct, '%')

    if key_pressed_list[pygame.K_DOWN]:
        scaleFromCenter = not (key_pressed_list[pygame.K_LSHIFT] or key_pressed_list[pygame.K_RSHIFT])
        if pct > 0:
            pct -= 10
        o_python_icon.scale(pct, scaleFromCenter=scaleFromCenter)
        # print('Scaling down to', pct, '%')

    # 8  Do any "per frame" actions
    counter += 1
    o_display_text_a.setValue("Here is some centered display text.\n" +
                              "Showing the \nnumber of frames.\nLoop counter:" + str(counter))

    o_display_text_b.setValue('Here is some display text.  Loop counter:' + str(counter))

    # 9 - Clear the window
    o_background_image.draw()

    # 10 - Draw all window elements
    o_python_icon.draw()
    o_display_text_title.draw()
    o_input_text_a.draw()
    o_input_text_b.draw()
    o_display_text_a.draw()
    o_display_text_b.draw()
    o_restart_button.draw()
    o_check_box_a.draw()
    o_radio_custom_1.draw()
    o_radio_custom_2.draw()
    o_radio_custom_3.draw()
    o_check_box_b.draw()
    o_radio_text_1.draw()
    o_radio_text_2.draw()
    o_radio_text_3.draw()
    o_status_button.draw()
    o_dragger.draw()
    o_image_collection.draw()
    o_frisbee_image.draw()
    o_image_instructions.draw()
    o_icon_instructions.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)   # make pygame wait

