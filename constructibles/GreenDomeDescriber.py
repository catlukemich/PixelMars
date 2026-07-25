from constructibles.GreenDome import GreenDome
from constructibles.PlaceableDescriber import PlaceableDescriber
from utils.Assets import loadImage


class GreenDomeDescriber(PlaceableDescriber):

    def getSpriteImage(self, tile):
        return loadImage("assets/green_dome.png")

    def createConstructible(self):
        return GreenDome(self.main.terrain)