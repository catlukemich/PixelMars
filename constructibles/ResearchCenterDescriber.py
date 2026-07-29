from constructibles.ConstructibleDescriber import ConstructibleDescriber
from constructibles.ResearchCenter import ResearchCenter
from utils.Assets import loadImage


class ResearchCenterDescriber(ConstructibleDescriber):

    def getSpriteImage(self, tile):
        return loadImage("assets/research_center.png")

    def createConstructible(self):
        return ResearchCenter(self.main.terrain)

    def getCost(self):
        return 15