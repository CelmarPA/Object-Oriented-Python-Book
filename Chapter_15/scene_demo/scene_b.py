# scene_b.py

# Scene B

from pygwidgets import DisplayText, TextButton
from pyghelpers import Scene
import pygame
from constants import *


class SceneB(Scene):

    def __init__(self, window: pygame.Surface) -> None:
        self.window: pygame.Surface = window

        self.message_field: DisplayText = DisplayText(self.window, (15, 25), "This is Scene B", fontSize=50,
                                                      textColor=WHITE, width=610, justified="center")

        self.go_to_a_button: TextButton = TextButton(window, (100, 100), "Go to Scene A")
        self.go_to_b_button: TextButton = TextButton(window, (250, 100), "Go to Scene B")
        self.go_to_c_button: TextButton = TextButton(window, (400, 100), "Go to Scene C")

        self.go_to_b_button.disable()

    def getSceneKey(self) -> str:
        return SCENE_B

    def handleInputs(self, events_list, key_pressed_list) -> None:
        for event in events_list:
            if self.go_to_a_button.handleEvent(event):
                self.goToScene(SCENE_A)

            if self.go_to_c_button.handleEvent(event):
                self.goToScene(SCENE_C)

            # Testing:  Press a or c to send message to those scenes
            #           Press or 1 or 3 to get data from A and C
            #           Press x to send message to all scenes

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.send(SCENE_A, SEND_MESSAGE, "Sending message to Scene A")

                if event.key == pygame.K_c:
                    self.send(SCENE_C, SEND_MESSAGE, "Sending message to Scene C")

                if event.key == pygame.K_1:
                    answer: str = self.request(SCENE_A, GET_DATA)
                    print("Received data from Scene A")
                    print(f"Answer was: {answer}")

                if event.key == pygame.K_3:
                    answer: str = self.request(SCENE_C, GET_DATA)
                    print("Received data from Scene C")
                    print(f"Answer was: {answer}")

                if event.key == pygame.K_x:
                    self.sendAll(SEND_MESSAGE, "Sending message to All scenes")

    def draw(self) -> None:
        self.window.fill(GRAY_B)

        self.message_field.draw()
        self.go_to_a_button.draw()
        self.go_to_b_button.draw()
        self.go_to_c_button.draw()

    def receive(self, receive_id, data) -> None:
        print("In B")
        print(f"Received a message of type: {receive_id}")
        print(f"The data received was: {data}")

    def respond(self, request_id) -> str | None:
        if request_id == GET_DATA:
            return "Here is data from scene A"

        return None
