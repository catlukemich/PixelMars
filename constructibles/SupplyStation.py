import pygame
from typing import Optional
from flyers.SupplyShip import SupplyShip
from utils.Assets import loadImage
from utils.Vectors import Vec3
from .Constructible import Constructible


class SupplyStation(Constructible):
    def __init__(self, terrain):
        from main.Game import Game

        Constructible.__init__(self, terrain, loadImage("assets/supply_station.png"))
        self.main: Optional[Game] = (
            None  # <-- Reference to main in order for the supply station to be able to do anything.
        )
        self.supply_time = 0

    def onPlace(self, main, tile):
        super().onPlace(main, tile)
        self.main = main
        supply_ship = SupplyShip.call(self, main)
        if self.main != None:
            self.main.view.addSprite(supply_ship)

    def update(self, clock: pygame.time.Clock):
        super().update(clock)
        self.supply_time += clock.get_time()

        if self.supply_time > 20000:
            self.supply_time = 0
            supply_ship = SupplyShip.call(self, self.main)
            if self.main != None:
                self.main.view.addSprite(supply_ship)
