from typing import Optional
from constructibles.PlaceableDescriber import PlaceableDescriber
from modes.ConnectorsRealigner import ConnectorsRealigner
from modes.WorldInteractionMode import WorldInteractionMode


class PlacementMode(WorldInteractionMode):

    def __init__(self, main):
        WorldInteractionMode.__init__(self, main)
        self.describer: Optional[PlaceableDescriber] = None
        self.tile_realigner = ConnectorsRealigner(main.terrain)


    def setPlaceableDescriber(self, describer):
        self.describer = describer

    def tileClicked(self, tile):
        if self.describer is None:
            return  # No describer set, cannot perform construction.
        if self.describer.canPlace(tile):
            self.describer.placeNew(tile)
            self.tile_realigner.realignConnectors(tile)
