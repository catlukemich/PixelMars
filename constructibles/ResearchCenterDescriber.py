from constructibles.PlaceableDescriber import PlaceableDescriber
from constructibles.ResearchCenter import ResearchCenter
from utils.Assets import loadImage


class ResearchCenterDescriber(PlaceableDescriber):

    def getSpriteImage(self, tile):
        return loadImage("assets/research_center.png")

    def createConstructible(self):
        return ResearchCenter(self.main.terrain)