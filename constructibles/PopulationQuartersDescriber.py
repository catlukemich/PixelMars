from constructibles.GreenDome import GreenDome
from constructibles.ConstructibleDescriber import ConstructibleDescriber
from constructibles.PopulationQuarters import PopulationQuarters
from utils.Assets import loadImage


class PopulationQuartersDescriber(ConstructibleDescriber):

    def getSpriteImage(self, tile):
        return loadImage("assets/population_quarters.png")

    def createConstructible(self):
        return PopulationQuarters(self.main.terrain)

    def getCost(self):
        return 10