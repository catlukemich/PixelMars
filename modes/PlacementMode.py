from typing import Optional
from constructibles.PlaceableDescriber import PlaceableDescriber
from modes.ConstructionMode import ConstructionMode


class PlacementMode(ConstructionMode):

    def __init__(self, main):
        ConstructionMode.__init__(self, main)
        self.describer: Optional[PlaceableDescriber] = None


    def setPlaceableDescriber(self, describer):
        self.describer = describer

    def performConstruction(self, tile):
        if self.describer is None:
            return  # No describer set, cannot perform construction.
        if self.describer.canPlace(tile):
            self.describer.placeNew(tile)
