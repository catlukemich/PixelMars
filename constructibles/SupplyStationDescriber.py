from constructibles.PlaceableDescriber import PlaceableDescriber
from constructibles.SupplyStation import SupplyStation
from utils.Assets import loadImage


class SupplyStationDescriber(PlaceableDescriber):

    def getSpriteImage(self, tile):
        return loadImage("assets/supply_station.png")

    def createConstructible(self):
        return SupplyStation(self.main.terrain)