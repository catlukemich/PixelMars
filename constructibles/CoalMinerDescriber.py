from constructibles.CoalMiner import CoalMiner
from constructibles.ConstructibleDescriber import ConstructibleDescriber
from terrain.CoalTile import CoalTile
from utils.Assets import loadImage


class CoalMinerDescriber(ConstructibleDescriber):

    def getSpriteImage(self, tile):
        return loadImage("assets/coal_miner.png")

    def createConstructible(self):
        return CoalMiner(self.main.terrain)

    def canPlace(self, tile):
        tiles = self.main.terrain.getSurroundingTilesPerpendicular(tile)
        for tile in tiles:
            if isinstance(tile, CoalTile):
                return True
        else: 
            return False
