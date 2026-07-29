import pygame

from VDebugger.vdebugger import vd
from utils.Vectors import Vec3
from view.Sprite import Sprite
from view.Updateable import Updateable


class Rot60Flyer(Sprite, Updateable):
    """
    This is a class for flyers(spaceshipis, supply shipis, assault ships) that can rotate in 24 directions.
    They use atlas with 24 images for rendering ship in each direction. The atlas has meet the following criteria.
    Atlas requirements:
    - It must start with an object facing up.
    - Each row must contain consecutive rotation images counterclockwise.
    - The last image must close the rotations cycle
        (initial rotation - delta rotation, where delta rotation is the amount the object rotates each frame)
    The total number of rows in atlas will be 5, same as rows - also 5, since 24 images only fit in 5x5 grid.

    The default rotation is 0 degrees - facing up, every next frame it adds delta rotation to the previous frame rotation.
    These are assumptions to make things simple and coherent.

    """

    def __init__(self, atlas: pygame.surface.Surface, single_image_size=48):
        super().__init__(atlas)
        self.atlas = atlas
        self.image_size = single_image_size
        self.rotation = 0

    def setAtlas(self, atlas):
        self.atlas = atlas

    def setRotation(self, rotation_degrees):
        rotation_degrees = rotation_degrees % 360
        self.rotation = rotation_degrees

    def getRotation(self):
        return self.rotation
        
    def update(self, clock):
        pass


    def draw(self, view, window: pygame.surface.Surface):
        index = round(self.rotation / 6)
        row = index // 8
        column = index % 8

        if self.visible:
            position = view.project(self.location)
            width = 48
            height = 48

            ## Calculate the position where the image will be drawn (offset it by half, so center is at the sprite position):
            draw_position = (position.x - width / 2, position.y - height / 2)

            ## Calculate the region of the atlas to use as a part of the source to draw from:
            # fmt: off
            draw_region = (
                column * self.image_size, row * self.image_size,
                self.image_size, self.image_size,
            )
            # fmt: on

            window.blit(self.image, draw_position, draw_region)
