from typing import Optional

from pygame import Clock

from constructibles.EnergyConsumer import EnergyConsumer
from terrain.CoalTile import CoalTile
from utils.Assets import loadImage
from view.Targetable import Targetable
from view.Updateable import Updateable
from .Constructible import Constructible


class CoalProcessor(Constructible, Updateable):
    """Coal processor processes coal into steel - get's 1 ton of coal every second and produces 1 ton of steel.
    It consumes 2 units of energy per second. """

    def __init__(self, terrain):
        Constructible.__init__(self, terrain, loadImage("assets/coal_processor.png"))
        self.processing_time = 0  # <-- Time counter to next harvest.
        self.energy_consumer: Optional[EnergyConsumer] = None

    def onPlace(self, main, tile):
        super().onPlace(main, tile)
        if self.main:
            self.energy_consumer = EnergyConsumer(self.main, 2)

    def update(self, clock: Clock):
        super().update(clock)

        self.processing_time += clock.get_time()
        if self.processing_time > 4000:
            self.processing_time = 0

            if self.main and self.energy_consumer:
                energy_consumed = self.energy_consumer.update(clock)
                if energy_consumed:
                    got_coal = self.main.player.subtractCoal(1)
                    if got_coal:
                        self.main.player.addSteel(1)
