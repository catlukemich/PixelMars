import pygame as pygame
import abc
from utils.Assets import loadImage
from constructibles.Connector import Connector
from view.Sprite import Sprite
from terrain.Tile import Tile
from modes.Mode import Mode


class ConstructionMode(Mode):

    def __init__(self, main):
        Mode.__init__(self, main)
        self.highlight = Sprite(loadImage("assets/highlight.png"))
        self.highlight.setLayer(2)
        self.highlight.setVisible(False)

    def enable(self):
        self.main.input.addListener(self)
        self.main.view.addSprite(self.highlight)

    def disable(self):
        self.main.input.removeListener(self)
        self.main.view.removeSprite(self.highlight)



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
                    self.performConstruction(tile)
                    self.realignConnectors(tile)

    @abc.abstractmethod
    def performConstruction(self, tile):
        pass


    def realignConnectors(self, tile):
        if tile.containsObject(Connector):
            connector = tile.getObject(Connector)
            connector.realignSelf(tile)

        surrounding = self.main.terrain.getSurroundingTilesPerpendicular(tile)
        for surrounding_tile in surrounding:
            if surrounding_tile.containsObject(Connector):
                connector = surrounding_tile.getObject(Connector)
                connector.realignSelf(surrounding_tile)
