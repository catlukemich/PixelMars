from random import Random

from terrain.Tile import Tile


class Terrain:
    def __init__(self, main):
        self.main = main

    def generate(self):
        self.width = 50
        self.height = 50

        self.tiles = []
        for y in range(0, self.width):
            for x in range(0, self.height):
                random = Random()
                # image_path = "tiles/tile_" + str(random.randint(0,8))
                image_path = "assets/tiles/tile_" + str(random.randint(1, 5)) + ".png"
                tile = Tile(image_path, x, y)
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


