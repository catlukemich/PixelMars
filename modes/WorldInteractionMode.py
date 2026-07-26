import pygame as pygame
import abc
from main import Constants
from utils.Assets import loadImage
from constructibles.Connector import Connector
from view.Sprite import Sprite
from terrain.Tile import Tile
from modes.Mode import Mode


class WorldInteractionMode(Mode):
    ''' In WorldInteractionMode a highlight on the world view is visible, this is an abstract class
    and inheriting classes should implement onTile click method, which is abstract. '''


    ###### Initialization with highlight loading: ######
    def __init__(self, main):
        Mode.__init__(self, main)
        self.highlight = Sprite(loadImage("assets/highlight.png"))
        self.highlight.setLayer(Constants.L2_OVERLAYS_LAYER)
        self.highlight.setVisible(False)

    ###### Disabling and enabling methods: ######
    def enable(self):
        self.main.input.addListener(self)
        self.main.view.addSprite(self.highlight)

    def disable(self):
        self.main.input.removeListener(self)
        self.main.view.removeSprite(self.highlight)

    ###### Event handling methods: ######
    def onEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.highlight.setVisible(False)
            view = self.main.view
            results = view.pick(event.pos[0], event.pos[1])
            for result in results:
                if isinstance(result, Tile):
                    self.highlight.setLocation(result.getLocation())
                    self.highlight.setVisible(True)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            view = self.main.view
            results = view.pick(event.pos[0], event.pos[1])
            for result in results:
                if isinstance(result, Tile):
                    tile = result
                    self.tileClicked(tile)
                   

    @abc.abstractmethod
    def tileClicked(self, tile):
        pass


    
