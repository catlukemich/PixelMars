from typing import Optional

from pygame import Clock

from constructibles.EnergyConsumer import EnergyConsumer
from utils.Assets import loadImage
from view.Updateable import Updateable
from .Constructible import Constructible


class PopulationQuarters(Constructible, Updateable):
    """ Population quarters can house up to 10 colonists. Every 10 colonists consume 10 t of food every 10 seconds. """

    def __init__(self, terrain):
        Constructible.__init__(self, terrain, loadImage("assets/population_quarters.png"))
        self.consumption_time = 0 # <-- Time counter to next harvest.
        self.energy_consumer: Optional[EnergyConsumer] = None
        self.quarter_capacity = 10
        self.quarter_occupation = 0
        
    def update(self, clock: Clock):
        self.consumption_time += clock.get_time()
        if self.consumption_time > 1000:
            self.consumption_time = 0
            if self.main and self.energy_consumer:
                energy_consumed = self.energy_consumer.update(clock)
                has_eaten = self.main.player.subtractFood(1)

                if self.quarter_occupation < self.quarter_capacity and has_eaten and energy_consumed:
                    self.quarter_occupation += 1
                    self.main.player.addPopulation(1)


    def onPlace(self, main, tile):
        super().onPlace(main, tile)
        if self.main:
            self.energy_consumer = EnergyConsumer(self.main, 10)


        