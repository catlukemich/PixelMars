import pygame


from VDebugger.vdebugger import vd
from utils.Vectors import Vec3


class Sprite():

    def __init__(self, image : pygame.Surface):
        self.location = Vec3()
        self.image = image
        self.layer = 0
        self.visible = True

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def setImage(self, image):
        self.image = image

    def getImage(self, image):
        return self.image

    def setLayer(self, layer):
        self.layer = layer

    def getLayer(self):
        return self.layer

    def setVisible(self, visible):
        self.visible = visible

    def draw(self, view, window):
        if self.visible:
            position = view.project(self.location)
            rect = self.image.get_rect()
            width = rect.width
            height = rect.height

            draw_pos = (position.x - width / 2, position.y - height /2)

            window.blit(self.image, draw_pos)

    def containsMouse(self, view, mouse_x, mouse_y):
        position = view.project(self.location)
        rect = self.image.get_rect()

        x = position.x
        y = position.y
        width = rect.width
        height = rect.height

        draw_x = x - width / 2
        draw_y = y - height / 2

        x_inside = mouse_x > draw_x and mouse_x < draw_x + width
        y_inside = mouse_y > draw_y and mouse_y < draw_y + height

        return x_inside and y_inside




