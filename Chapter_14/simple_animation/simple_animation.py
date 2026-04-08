# simple_animation.py

# SimpleAnimation class

import pygame
import time


class SimpleAnimation:

    def __init__(self, window: pygame.Surface, loc: tuple[int, int],
                 pic_paths: tuple[str, ...], duration_per_image: float) -> None:
        self.window: pygame.Surface = window
        self.loc: tuple[int, int] = loc
        self.images_list: list[pygame.Surface] = []

        for pic_path in pic_paths:
            image: pygame.Surface = pygame.image.load(pic_path)     # load an image
            image = pygame.Surface.convert_alpha(image)     # optimize blitting
            self.images_list.append(image)

        self.playing: bool = False
        self.duration_per_image: float = duration_per_image
        self.n_images: int = len(self.images_list)
        self.index: int = 0
        self.image_start_time: float = 0.0
        self.elapsed: float = 0.0

    def play(self) -> None:
        if self.playing:
            return

        self.playing = True
        self.image_start_time = time.time()
        self.index = 0

    def update(self) -> None:
        if not self.playing:
            return

        # How much time has elapsed since we started showing this image
        self.elapsed = time.time() - self.image_start_time

        # If enough time has elapsed, move onto the next image
        if self.elapsed > self.duration_per_image:
            self.index += 1

            if self.index < self.n_images:  # move on to next image
                self.image_start_time = time.time()

            else:   # animation is finished
                self.playing = False
                self.index = 0  # reset to the beginning

    def draw(self) -> None:
        # Assumes that self.index has been set earlier - in update() method.
        # It is used as the index into the imagesList to find the current image.
        the_image: pygame.Surface = self.images_list[self.index]    # choose the image to show

        self.window.blit(the_image, self.loc)  # show it
