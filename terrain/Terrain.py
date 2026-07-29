from random import Random
import random

from terrain.CoalTile import CoalTile
from terrain.Tile import Tile


class Terrain:
    def __init__(self, main):
        self.main = main

    def generate(self):
        self.width = 50
        self.height = 50

        ###### Terrain generation: ######
        self.tiles = []
        for y in range(0, self.width):
            for x in range(0, self.height):
                prob_has_resource = random.randint(1,300)
                if prob_has_resource == 300:
                    tile = CoalTile("assets/tiles/coal_tile.png", x, y)
                else:
                    prob_other_than_flat = random.randint(1,5)
                    if prob_other_than_flat == 1:
                        image_path = "assets/tiles/tile_" + str(random.randint(1, 12)) + ".png"
                        tile = Tile(image_path, x, y)
                    else:
                        tile = Tile("assets/tiles/tile_3.png",x, y)
                self.tiles.append(tile)
                self.main.view.addSprite(tile)

    def getSurroundingTiles(self, tile):
        start_x = tile.x - 1
        end_x = tile.x + 1
        start_y = tile.y - 1
        end_y = tile.y + 1

        tiles = []
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                tile = self.getTile(x, y)
                if tile is not None:
                    tiles.append(tile)

        return tiles

    def getSurroundingTilesPerpendicular(self, tile):
        tile_north = self.getTile(tile.x, tile.y - 1)
        tile_south = self.getTile(tile.x, tile.y + 1)
        tile_west = self.getTile(tile.x - 1, tile.y)
        tile_east = self.getTile(tile.x + 1, tile.y)

        tiles = []

        if tile_north is not None:
            tiles.append(tile_north)
        if tile_south is not None:
            tiles.append(tile_south)
        if tile_west is not None:
            tiles.append(tile_west)
        if tile_east is not None:
            tiles.append(tile_east)

        print(tiles)

        return tiles


    def getTile(self, x, y) -> Tile:
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            raise Exception(f"Tile {x}, {y} is out of map")
        index = y * self.width + x
        return self.tiles[index]


