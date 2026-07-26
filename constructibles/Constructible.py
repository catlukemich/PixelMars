from main import Constants
from view.Sprite import Sprite


class Constructible(Sprite):
    def __init__(self, terrain, image, destructible = True):
        Sprite.__init__(self, image)
        self.terrain = terrain
        self.layer = Constants.L3_CONSTRUCTIBLES_LAYER
        self.destructible = destructible
