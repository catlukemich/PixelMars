from flyers.Starship import Starship
from main import Constants
from utils.Assets import loadImage
from .Constructible import Constructible


class Connector(Constructible):
    '''
    Connectors are buildable elements that interconnect to other important buildings like green dome or supply station.
    '''
    def __init__(self, terrain, image):
        Constructible.__init__(self, terrain, image)

    def realignSelf(self, tile):
        if tile.containsObject(Connector):
            terrain = self.terrain
            tile_north = terrain.getTile(tile.x, tile.y - 1)
            tile_south = terrain.getTile(tile.x, tile.y + 1)
            tile_west = terrain.getTile(tile.x - 1, tile.y)
            tile_east = terrain.getTile(tile.x + 1, tile.y)

            image_path = self.getImagePath(tile_north, tile_south, tile_west, tile_east)
            self.image = loadImage(image_path)

    def getImagePath(self, tile_north, tile_south, tile_west, tile_east):
        north_string = "n" if tile_north != None and tile_north.containsObject(Constructible) or tile_north.containsObject(Starship) else ""
        south_string = "s" if tile_south != None and tile_south.containsObject(Constructible) or tile_south.containsObject(Starship) else ""
        west_string = "w" if tile_west != None and tile_west.containsObject(Constructible) or tile_west.containsObject(Starship) else ""
        east_string = "e" if tile_east != None and tile_east.containsObject(Constructible) or tile_east.containsObject(Starship) else ""
        image_path = "assets/connectors/connector_" + north_string + south_string + west_string + east_string + ".png"
        return image_path
