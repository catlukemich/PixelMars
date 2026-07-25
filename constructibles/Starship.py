from utils.Assets import loadImage
from .Constructible import Constructible


class Starship(Constructible):

    def __init__(self, terrain):
        Constructible.__init__(self, terrain, loadImage("assets/starship.png"), False)
        self.thrusters_enabled = loadImage("assets/starship_thrusters.png")
        self.thrusters_disabled = loadImage("assets/starship.png")


    def toggleThrusters(self, enabled):
        if enabled:
            self.setImage(self.thrusters_enabled)
        else:
            self.setImage(self.thrusters_disabled)