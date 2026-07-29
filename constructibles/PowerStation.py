from typing import Optional

from pygame import Clock

from terrain.CoalTile import CoalTile
from utils.Assets import loadImage
from view.Targetable import Targetable
from view.Updateable import Updateable
from .Constructible import Constructible


class PowerStation(Constructible, Updateable):
    """ Power station generates energy from sun - it provides 4 mWh of energy every second. """

    def __init__(self, terrain):
        Constructible.__init__(self, terrain, loadImage("assets/power_station.png"))
        self.generation_time = 0

    def update(self, clock: Clock):
        super().update(clock)
        self.generation_time += clock.get_time()
        if self.generation_time > 1000:
            self.generation_time = 0
            if self.main:
                self.main.player.addEnergy(4)
    

  
