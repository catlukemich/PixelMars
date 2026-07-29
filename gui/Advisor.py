import pygame

from gui.AnimatedIcon import AnimatedIcon
from gui.Icon import Icon
from gui.Label import Label
from gui.Panel import Panel
from utils.Assets import loadImage
from utils.Speech import Speech


class Advisor:
    """A blonde woman Anna giving advices (memo) - a gui component with panel, advisor's face, handling messages and supporting
    cursor if a message is associated with certain point on the map."""

    def __init__(self, main) -> None:
        from main.Game import Game

        self.main: Game = main

        self.visible = False

        ###### The panel behind, the woman, the message and the target button: ######
        self.panel = Panel(800, 100)
        self.panel.setPosition((0, 480))

        self.advisor_face = AnimatedIcon(
            loadImage("assets/gui/woman_atlas.png"), 4, 320 // 4, 80
        )
        self.advisor_face.setPosition((10, 490))

        self.message = Label("", 14)
        self.message.setPosition((100, 500))

        # Flag indicating if the crosshair should be shown - used internally 
        # - disabled when using "communicate", enabled when using "communicateWithCrosshair":
        self.show_crosshair = False  

        self.crosshair = Icon(loadImage("assets/gui/crosshair.png"))
        self.crosshair.setPosition((750, 500))

        self.reading = False
        self.reading_time = 0
        self.read_time = 0

        self.end_listener = None
        self.crosshair_listener = None

    def show(self):
        if not self.visible:
            self.visible = True
            self.main.gui.addWidget(self.panel)
            self.main.gui.addWidget(self.advisor_face)
            self.main.gui.addWidget(self.message)
            if self.show_crosshair:
                self.main.gui.addWidget(self.crosshair)

    def hide(self):
        if self.visible:
            self.visible = False
            self.main.gui.removeWidget(self.panel)
            self.main.gui.removeWidget(self.advisor_face)
            self.main.gui.removeWidget(self.message)
            if self.show_crosshair:
                self.main.gui.removeWidget(self.crosshair)

    def communicate(self, message, end_listener=None):
        ''' Communicate a message to the user, providing an end listener, which fires, when the message is "read" by the advisor, by default every character
        in the message takes some time to read. '''
        self.show()
        self.read_time = len(message * 50)
        self.reading = True
        self.message.setText(message)
        self.end_listener = end_listener

    def communicateWithTarget(self, message, end_listener=None, crosshair_listener=None):
        ''' Communicate a message to the player with support for the crosshair - when player clicks the crosshair the crosshair listener gets triggered. '''
        self.show_crosshair = True
        self.crosshair.click_listener = self
        self.crosshair_listener = crosshair_listener
        self.communicate(message, end_listener)

    def update(self, clock: pygame.time.Clock):
        if not self.reading:
            return

        self.reading_time += clock.get_time()
        if self.reading_time > self.read_time:
            self.reading_time = 0
            self.reading = False
            self.hide()
            self.show_crosshair = False
            if self.end_listener:
                self.end_listener()

    def onClick(self, event, widget):
        if widget == self.crosshair and self.crosshair_listener:
            self.crosshair_listener()
