from pygame import Clock
from typing import Optional
from constructibles.EnergyConsumer import EnergyConsumer
from terrain.CoalTile import CoalTile
from utils.Assets import loadImage
from view.Targetable import Targetable
from view.Updateable import Updateable
from .Constructible import Constructible


class CoalMiner(Constructible, Updateable):
    def __init__(self, terrain):
        Constructible.__init__(self, terrain, loadImage("assets/coal_miner.png"))
        self.harvest_time = 0  # <-- Time counter to next harvest.
        self.energy_consumer: Optional[EnergyConsumer] = None
        self.targetable: Optional[Targetable] = None


    def onPlace(self, main, tile):
        super().onPlace(main, tile)
        if self.main:
            self.energy_consumer = EnergyConsumer(self.main, 1)


    def update(self, clock: Clock):
        # fmt: off
        self.harvest_time += clock.get_time()
        if self.harvest_time > 1000:
            self.harvest_time = 0
            if self.main and self.energy_consumer:
                energy_consumed = self.energy_consumer.update(clock)
                if energy_consumed:
                    tiles = self.main.terrain.getSurroundingTilesPerpendicular(self.tile)
                    for tile in tiles: # <-- Keep in mind, that the more coal tiles surround a coal miner, the more coal it will extract.
                        if isinstance(tile, CoalTile):
                            if tile.isCoalExhausted(): continue
                            digged = tile.digCoal(1)
                            if digged: self.main.player.addCoal(1) # <-- Add some coal every second if there is enough coal in coal deposits around.
                            else: 
                                # <-- The deposit has exhausted.
                                tile.setImage(loadImage("assets/tiles/tile_6.png"))
                                self.main.advisor.communicateWithTarget("The deposit at coal mine has been exhausted", crosshair_listener=self.centerView)
                
        # fmt: on

        if self.targetable:
            self.targetable.update(clock)
        if self.main:
            if self.targetable and not self.targetable.hasFinished():
                self.main.view.setCenter(self.targetable.getLocation())

    def centerView(self):
        if self.main:
            self.targetable = Targetable(self.main.view, self)
            self.main.view.setCenter(self.targetable.getLocation())
