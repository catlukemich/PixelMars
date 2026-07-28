from main import Constants
from utils.Assets import loadImage
from view.Sprite import Sprite


class Starship(Sprite):

    def __init__(self, terrain):
        super().__init__(loadImage("assets/starship.png"))
        self.thrusters_enabled = loadImage("assets/starship_thrusters.png")
        self.thrusters_disabled = loadImage("assets/starship.png")
        self.setLayer(Constants.L3_CONSTRUCTIBLES_LAYER)


    def toggleThrusters(self, enabled):
        if enabled:
            self.setImage(self.thrusters_enabled)
        else:
            self.setImage(self.thrusters_disabled)