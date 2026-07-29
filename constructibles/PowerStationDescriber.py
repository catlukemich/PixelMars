from constructibles.PowerStation import PowerStation
from constructibles.CoalMiner import CoalMiner
from constructibles.ConstructibleDescriber import ConstructibleDescriber
from terrain.CoalTile import CoalTile
from utils.Assets import loadImage


class PowerStationDescriber(ConstructibleDescriber):

    def getSpriteImage(self, tile):
        return loadImage("assets/power_station.png")

    def createConstructible(self):
        return PowerStation(self.main.terrain)

    def getCost(self):
        return 5