from utils.Assets import loadImage
from .Constructible import Constructible


class ResearchCenter(Constructible):
    """ Research center is responsible for deploying a Mars rover, to discover new lands and coal resources. TODO """

    def __init__(self, terrain):
        Constructible.__init__(self, terrain, loadImage("assets/research_center.png"))