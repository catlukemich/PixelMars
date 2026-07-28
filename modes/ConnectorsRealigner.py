from constructibles.Connector import Connector


class ConnectorsRealigner():

    def __init__(self, terrain) -> None:
        self.terrain = terrain

    def realignConnectors(self, tile):
        if tile.containsObject(Connector):
            connector = tile.getObject(Connector)
            connector.realignSelf(tile)

        surrounding = self.terrain.getSurroundingTilesPerpendicular(tile)
        for surrounding_tile in surrounding:
            if surrounding_tile.containsObject(Connector):
                connector = surrounding_tile.getObject(Connector)
                try:
                    connector.realignSelf(surrounding_tile)
                except:
                    pass # <-- The tile is out of map.