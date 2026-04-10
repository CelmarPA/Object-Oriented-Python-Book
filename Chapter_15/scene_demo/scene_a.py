# scene_a.py

# Scene A

from pygwidgets import DisplayText, TextButton
from pyghelpers import Scene
import pygame
from constants import *


class SceneA(Scene):

    def __init__(self, window: pygame.Surface) -> None:
        self.window: pygame.Surface = window

        self.message_field: DisplayText = DisplayText(self.window, (15, 25), "This is Scene A", fontSize=50,
                                                      textColor=WHITE, width=610, justified="center")

        self.go_to_a_button: TextButton = TextButton(window, (100, 100), "Go to Scene A")
        self.go_to_b_button: TextButton = TextButton(window, (250, 100), "Go to Scene B")
        self.go_to_c_button: TextButton = TextButton(window, (400, 100), "Go to Scene C")

        self.go_to_a_button.disable()

    def getSceneKey(self) -> str:
        return SCENE_A

    def handleInputs(self, events_list, key_pressed_list) -> None:
        for event in events_list:
            if self.go_to_b_button.handleEvent(event):
                self.goToScene(SCENE_B)

            if self.go_to_c_button.handleEvent(event):
                self.goToScene(SCENE_C)

            # Testing:  Press b or c to send message to those scenes
            #           Press or 2 or 3 to get data from B and C
            #           Press x to send message to all scenes

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    self.send(SCENE_B, SEND_MESSAGE, "Sending message to Scene B")

                if event.key == pygame.K_c:
                    self.send(SCENE_C, SEND_MESSAGE, "Sending message to Scene C")

                if event.key == pygame.K_2:
                    answer: str = self.request(SCENE_B, GET_DATA)
                    print("Received data from Scene B")
                    print(f"Answer was: {answer}")

                if event.key == pygame.K_3:
                    answer: str = self.request(SCENE_C, GET_DATA)
                    print("Received data from Scene C")
                    print(f"Answer was: {answer}")

                if event.key == pygame.K_x:
                    self.sendAll(SEND_MESSAGE, "Sending message to All scenes")

    def draw(self) -> None:
        self.window.fill(GRAY_A)

        self.message_field.draw()
        self.go_to_a_button.draw()
        self.go_to_b_button.draw()
        self.go_to_c_button.draw()

    def receive(self, receive_id, data) -> None:
        print("In A")
        print(f"Received a message of type: {receive_id}")
        print(f"The data received was: {data}")

    def respond(self, request_id) -> str | None:
        if request_id == GET_DATA:
            return "Here is data from scene A"

        return None
