

import pygame

from gui.Widget import Widget


class Label(Widget):

    def __init__(self, text = "", font_size = 8, font = None, color = (0,0,0)):
        super().__init__()
        self.text = text
        self.font_size = font_size
        self.font = font
        self.color = color

    def setColor(self, color):
        self.color = color

    def draw(self, window):
        font = pygame.font.Font("assets/fonts/DejaVuSans.ttf", self.font_size) if self.font is None else self.font
        text_surface = font.render(self.text, True, self.color)
        window.blit(text_surface, self.position)

    def setText(self, text):
        self.text = text