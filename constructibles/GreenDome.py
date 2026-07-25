from utils.Assets import loadImage
from .Constructible import Constructible


class GreenDome(Constructible):
    def __init__(self, terrain):
        Constructible.__init__(self, terrain, loadImage("assets/green_dome.png"))