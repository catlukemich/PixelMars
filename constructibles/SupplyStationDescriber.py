from constructibles.ConstructibleDescriber import ConstructibleDescriber
from constructibles.SupplyStation import SupplyStation
from utils.Assets import loadImage


class SupplyStationDescriber(ConstructibleDescriber):

    def getSpriteImage(self, tile):
        return loadImage("assets/supply_station.png")

    def createConstructible(self):
        return SupplyStation(self.main.terrain)