import pygame
from typing import Optional
from constructibles.EnergyConsumer import EnergyConsumer
from flyers.SupplyShip import SupplyShip
from utils.Assets import loadImage
from utils.Vectors import Vec3
from .Constructible import Constructible


class SupplyStation(Constructible):
    """ Supply stations allow supply ships to provide the colony with some random resources. But they require energy in order to operate. """

    def __init__(self, terrain):
        from main.Game import Game
        Constructible.__init__(self, terrain, loadImage("assets/supply_station.png"))
        self.main: Optional[Game] = None
        self.energy_consumer: Optional[EnergyConsumer] = None
        self.supply_time = 0

    def onPlace(self, main, tile):
        super().onPlace(main, tile)
        
        if self.main != None:
            supply_ship = SupplyShip.call(self, main)
            self.energy_consumer = EnergyConsumer(self.main, 1)
            self.main.view.addSprite(supply_ship)

    def update(self, clock: pygame.time.Clock):
        super().update(clock)
        self.supply_time += clock.get_time()

        if self.supply_time > 20000:
            self.supply_time = 0
            if self.main and self.energy_consumer:
                supply_ship = SupplyShip.call(self, self.main)
                self.main.view.addSprite(supply_ship)
