

import pygame

from gui.Label import Label
from gui.Panel import Panel


class Communicator():


    def __init__(self, main) -> None:
        from main.Game import Game
        self.main: Game = main
        self.queue = []
        self.reading_time = 0
        self.read_time = 0

        self.visible = False

        self.message_panel = Panel(800, 15, (0,0,0)) # pyright: ignore
        self.message_panel.setPosition((0, 585))

        self.message_label = Label("", 12)
        self.message_label.setColor((255,50,50))
        self.message_label.setPosition((10, 585))


    def communicate(self, message):
        if not self.visible:
            self.read_time = len(message) * 50
            self.message_label.setText(message)
            self.main.gui.addWidget(self.message_panel)
            self.main.gui.addWidget(self.message_label)
            self.visible = True
            


    def update(self, clock: pygame.time.Clock):
        if self.visible:
            self.reading_time += clock.get_time()
            if self.reading_time > self.read_time:
                self.reading_time = 0
                self.main.gui.removeWidget(self.message_panel)
                self.main.gui.removeWidget(self.message_label)
                self.visible = False


