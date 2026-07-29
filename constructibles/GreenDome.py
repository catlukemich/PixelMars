from pygame import Clock

from utils.Assets import loadImage
from view.Updateable import Updateable
from .Constructible import Constructible


class GreenDome(Constructible, Updateable):
    def __init__(self, terrain):
        Constructible.__init__(self, terrain, loadImage("assets/green_dome.png"))
        self.harvest_time = 0 # <-- Time counter to next harvest.

    def update(self, clock: Clock):
        self.harvest_time += clock.get_time()
        if self.harvest_time > 1000:
            self.harvest_time = 0
            if self.main:
                self.main.player.addFood(1)
        