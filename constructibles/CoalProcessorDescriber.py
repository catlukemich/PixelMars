from constructibles.CoalMiner import CoalMiner
from constructibles.CoalProcessor import CoalProcessor
from constructibles.ConstructibleDescriber import ConstructibleDescriber
from terrain.CoalTile import CoalTile
from utils.Assets import loadImage


class CoalProcessorDescriber(ConstructibleDescriber):

    def getSpriteImage(self, tile):
        return loadImage("assets/coal_processor.png")

    def createConstructible(self):
        return CoalProcessor(self.main.terrain)

    def getCost(self):
        return 5