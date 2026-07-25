from main.Constants import TILE_HEIGHT, TILE_WIDTH, VIEW_WIDTH, VIEW_HEIGHT
from functools import cmp_to_key

from utils.Vectors import Vec3, Vec2
from view.Updateable import Updateable


class View:
    '''
    View class is responsible for displaying a view inside a main window.
    (TODO: Perhaps implement multiple viewports)
    '''
    def __init__(self):
        self.center = Vec3(0, 0, 0)  # <-- Center of the 2D View
        self.sprites = [] # <-- List of 2D view underlying sprites

    def addSprite(self, sprite):
        ''' Add sprite to the view.'''
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        ''' Remove sprite from the view. '''
        self.sprites.remove(sprite)

    def getCenter(self):
        ''' Get the center of the view. '''
        return Vec3(self.center.x, self.center.y, self.center.z)

    def setCenter(self, center):
        ''' Set the center of the view. '''
        self.center = center

    def update(self, clock):
        ''' Update the view and it's underlying sprites. '''
        for sprite in self.sprites:
            if isinstance(sprite, Updateable):
                sprite.update(clock)


    def draw(self, window):
        ''' Draw the view by sorting and drawing it's underlying sprites, that are in a list. '''
        self.sprites.sort(key = cmp_to_key(self._compareSprites))

        for sprite in self.sprites:
            sprite.draw(self, window)


    def _compareSprites(self, sprite1, sprite2):
        ''' 
        Compare 2 sprites for sorting 
        - simply compare their layer, and if they are the same - compare the y position,
        thi is called y sorting 
        '''
        if sprite1.layer == sprite2.layer:
            return sprite1.location.y - sprite2.location.y
        else:
            return sprite1.layer - sprite2.layer


    def project(self, location):
        ''' Project from world pseudo 3D location to screen 2D location 
        - that also depends on where is the center of the View. '''
        x = location.x
        y = location.y
        z = location.z

        view_x = (x - self.center.x) * TILE_WIDTH
        view_y = (y - self.center.y - z + self.center.z) * TILE_HEIGHT

        view_x += VIEW_WIDTH / 2
        view_y += VIEW_HEIGHT / 2

        return Vec2(view_x, view_y)


    def pick(self, x, y):
        ''' Pick some sprites using 2D screen coordinates. '''
        results = []
        for sprite in self.sprites:
            if sprite.containsMouse(self, x, y):
                results.append(sprite)
        return results