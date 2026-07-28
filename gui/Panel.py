

import pygame

from gui.Widget import Widget


class Panel(Widget):

    def __init__(self, width, height, color = pygame.Color((255,255,255))):
        super().__init__()
        self.size = (width, height)
        self.color = color


    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.position[0], self.position[1], self.size[0], self.size[1]), 0, 0)
        

