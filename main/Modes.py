from modes.ClearMode import ClearMode
from modes.Mode import Mode
from modes.ConstructionMode import PlacementMode

class Modes:
    def __init__(self, main):
        self.main = main

        self.current_mode = Mode(main)
        self.placement_mode = PlacementMode(main)
        self.clear_mode = ClearMode(main)
