
# Constructibles imports:
import abc

from constructibles.Constructible import Constructible
from flyers.Starship import Starship
from utils.Vectors import Vec3

class ConstructibleDescriber:
    ''' The placeable describer is responsible for describing how a constructible can be placed on the terrain,
    what sprite to use when placed on the surface of Mars 
    It provides methods to check if a constructible can be placed on a given tile. '''

    def __init__(self, main):
        from main.Game import Game
        self.main : Game = main

    def getSpriteImage(self, tile):
        pass

    def placeNew(self, tile):
        constructible = self.createConstructible()
        constructible.setLocation(Vec3(tile.x, tile.y, 0))
        self.main.view.addSprite(constructible)
        tile.addObject(constructible)
        return constructible

    @abc.abstractmethod
    def createConstructible(self) -> Constructible:
        pass

    def canPlace(self, tile):
        if tile.containsObject(Constructible):
            return False  # Already occupied

        terrain = self.main.terrain
        surrounding_perp = terrain.getSurroundingTilesPerpendicular(tile)
        for tile in surrounding_perp:
            if tile.containsObject(Constructible) or tile.containsObject(Starship):
                return True
        return False






    




