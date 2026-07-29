from typing import Optional
from VDebugger.vdebugger import vd
from constructibles.ConstructibleDescriber import ConstructibleDescriber
from modes.ConnectorsRealigner import ConnectorsRealigner
from modes.WorldInteractionMode import WorldInteractionMode
from utils.Assets import loadSound


class PlacementMode(WorldInteractionMode):

    def __init__(self, main):
        WorldInteractionMode.__init__(self, main)
        self.describer: Optional[ConstructibleDescriber] = None
        self.tile_realigner = ConnectorsRealigner(main.terrain)

    def setPlaceableDescriber(self, describer):
        self.describer = describer

    def tileClicked(self, tile):
        if self.describer is None:
            return  # No describer set, cannot perform construction.


        can_place = self.describer.canPlace(tile)
        if can_place:
            ## Firstly check if the amount of steel is available for construction:
            steel_cost = self.describer.getCost()
            if steel_cost > self.main.player.getSteel(): # <-- Not enough steel to construct.
                self.main.communicator.communicate("Not enough steel to place, required: " + str(steel_cost) + " tons.")
                loadSound("assets/sounds/beep.ogg").play()
                return
            else:
                self.main.player.subtractSteel(steel_cost)
            constructible = self.describer.placeNew(tile)
            constructible.onPlace(self.main, tile)
            self.tile_realigner.realignConnectors(tile)

            loadSound("assets/sounds/automatic_hammer.wav").play()
