import pygame

from gui.Widget import Widget

class Button(Widget):
    def __init__(self, image):
        Widget.__init__(self)
        self.image = image
        rect = image.get_rect()
        self.size = (rect.width, rect.height)

    def draw(self, window):
        x = self.position[0]
        y = self.position[1]
        width = self.size[0]
        height = self.size[1]
        window.fill((255,255,255), (x,y ,width, height))
        window.blit(self.image, self.position)
        pygame.draw.rect(window, (0, 0, 0), (x, y, width, height),1)


