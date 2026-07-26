from constructibles.Constructible import Constructible
from modes.WorldInteractionMode import WorldInteractionMode


class ClearMode(WorldInteractionMode):

    def __init__(self, main):
        WorldInteractionMode.__init__(self, main)

    def tileClicked(self, tile):
        constructible = tile.getObject(Constructible)
        if constructible != None and constructible.destructible:
            self.main.view.removeSprite(constructible)
            tile.removeObject(constructible)
