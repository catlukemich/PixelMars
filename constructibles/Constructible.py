import pygame
from typing import Optional
from flyers.SupplyShip import SupplyShip
from main import Constants
from terrain.Tile import Tile
from view.Sprite import Sprite
from view.Updateable import Updateable


class Constructible(Sprite, Updateable):
    def __init__(self, terrain, image, destructible=True):
        Sprite.__init__(self, image)
        self.terrain = terrain
        self.layer = Constants.L3_CONSTRUCTIBLES_LAYER
        self.destructible = destructible
        from main.Game import Game
        self.main : Optional[Game] = None
        self.tile : Optional[Tile] = None

    def onPlace(self, main, tile):
        self.main = main
        self.tile = tile
        """
        The onPlace is a stub method.
        it get's as DI the whole main class, so any constructible, when placed can perform any action.
        """
        pass
