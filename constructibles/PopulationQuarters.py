from pygame import Clock

from utils.Assets import loadImage
from view.Updateable import Updateable
from .Constructible import Constructible


class PopulationQuarters(Constructible, Updateable):
    def __init__(self, terrain):
        Constructible.__init__(self, terrain, loadImage("assets/population_quarters.png"))
        self.consumption_time = 0 # <-- Time counter to next harvest.

    def update(self, clock: Clock):
        self.consumption_time += clock.get_time()
        if self.consumption_time > 10000:
            self.consumption_time = 0
            if self.main:
                self.main.player.subtractFood(10)

    def onPlace(self, main, tile):
        super().onPlace(main, tile)
        if self.main:
            self.main.player.addPopulation(10)
        