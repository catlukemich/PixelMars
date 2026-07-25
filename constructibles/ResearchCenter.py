from utils.Assets import loadImage
from .Constructible import Constructible


class ResearchCenter(Constructible):
    def __init__(self, terrain):
        Constructible.__init__(self, terrain, loadImage("assets/research_center.png"))