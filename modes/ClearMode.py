from constructibles.Constructible import Constructible
from modes.ConstructionMode import ConstructionMode


class ClearMode(ConstructionMode):

    def __init__(self, main):
        ConstructionMode.__init__(self, main)

    def performConstruction(self, tile):
        constructible = tile.getObject(Constructible)
        if constructible != None and constructible.destructible:
            self.main.view.removeSprite(constructible)
            tile.removeObject(constructible)
