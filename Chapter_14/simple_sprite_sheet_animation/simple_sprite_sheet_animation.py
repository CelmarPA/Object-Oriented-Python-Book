# simple_sprite_sheet_animation.py

# SimpleSpriteSheetAnimation class

import pygame
import time


class SimpleSpriteSheetAnimation:

    def __init__(self, window: pygame.Surface, loc: tuple[int, int], image_path: str,
                 n_images: int, width: int, height: int, duration_per_image: float) -> None:
        self.window: pygame.Surface = window
        self.loc: tuple[int, int] = loc
        self.n_images: int = n_images
        self.images_list: list[pygame.Surface] = []

        # Load the sprite sheet
        sprite_sheet_image: pygame.Surface = pygame.image.load(image_path)
        # Optimizes blitting
        sprite_sheet_image = sprite_sheet_image.convert_alpha()

        # Calculate the number of columns in the starting image
        n_cols: int = sprite_sheet_image.get_width() // width

        # Break the starting image into subimages
        row: int = 0
        col: int = 0

        for image_number in range(n_images):
            x: int = col * width
            y: int = row * height

            # Create a subsurface from the bigger spriteSheet
            sub_surface_rect: pygame.Rect = pygame.Rect(x, y, width, height)
            image: pygame.Surface = sprite_sheet_image.subsurface(sub_surface_rect)
            self.images_list.append(image)

            col += 1
            if col == n_cols:
                col = 0
                row += 1

        self.duration_per_image: float = duration_per_image
        self.playing: bool = False
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
        # Assumes that self.index has been set earlier - in the update() method.
        # It is used as the index into the imagesList to find the current image.
        the_image: pygame.Surface = self.images_list[self.index]    # choose the image to show

        self.window.blit(the_image, self.loc)   #show it
