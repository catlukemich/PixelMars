from typing import Optional

from pygame import Clock

from main import Constants
from utils.Assets import loadImage
from view.Sprite import Sprite
from view.Updateable import Updateable


class Starship(Sprite, Updateable):

    def __init__(self, terrain):
        super().__init__(loadImage("assets/starship.png"))
        from main.Game import Game
        self.main: Optional[Game] = None
        self.thrusters_enabled = loadImage("assets/starship_thrusters.png")
        self.thrusters_disabled = loadImage("assets/starship.png")
        self.setLayer(Constants.L3_CONSTRUCTIBLES_LAYER)
        self.providing_time = 0

    def toggleThrusters(self, enabled):
        if enabled:
            self.setImage(self.thrusters_enabled)
        else:
            self.setImage(self.thrusters_disabled)

    def onLanding(self, main):
        self.main = main


    def update(self, clock: Clock):
        super().update(clock)
        self.providing_time += clock.get_time()
        if self.providing_time > 1000:
            self.providing_time = 0
            if self.main:
                self.main.player.addEnergy(2)
                self.main.player.subtractFood(1)

