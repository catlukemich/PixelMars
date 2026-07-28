from typing import Optional
from VDebugger.vdebugger import vd
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

        can_place = self.describer.canPlace(tile)
        if can_place:
            constructible = self.describer.placeNew(tile)
            constructible.onPlace(self.main)
            self.tile_realigner.realignConnectors(tile)
            
