from constructibles.Connector import Connector
from constructibles.Constructible import Constructible
from constructibles.PlaceableDescriber import PlaceableDescriber
from utils.Assets import loadImage


class ConnectorPlaceableDescriber(PlaceableDescriber):

    def getSpriteImage(self, tile):
        terrain = self.main.terrain
        surrounding = terrain.getSurroundingTilesPerpendicular(tile)
        north_string = south_string = west_string = east_string = ""
        if surrounding[0].containsObject(Constructible): north_string = "n"
        if surrounding[1].containsObject(Constructible): south_string = "s"
        if surrounding[2].containsObject(Constructible): west_string = "w"
        if surrounding[3].containsObject(Constructible): east_string = "e"
        image_path = "assets/connectors/connector_" + north_string + south_string + west_string + east_string + ".png"
        return loadImage(image_path)


    def createConstructible(self):
        connector = Connector(self.main.terrain, None)
        return connector