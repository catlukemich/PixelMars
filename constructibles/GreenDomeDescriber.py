from constructibles.GreenDome import GreenDome
from constructibles.ConstructibleDescriber import ConstructibleDescriber
from utils.Assets import loadImage


class GreenDomeDescriber(ConstructibleDescriber):

    def getSpriteImage(self, tile):
        return loadImage("assets/green_dome.png")

    def createConstructible(self):
        return GreenDome(self.main.terrain)