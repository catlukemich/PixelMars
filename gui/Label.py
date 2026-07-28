

import pygame

from gui.Widget import Widget


class Label(Widget):

    def __init__(self, text = "", font_size = 10):
        super().__init__()
        self.text = text
        self.font_size = font_size

    def draw(self, window):
        font = pygame.font.Font("assets/fonts/ArchivoNarrow-Regular.ttf", self.font_size)
        text_surface = font.render(self.text, True, (0,0,0))
        window.blit(text_surface, self.position)
