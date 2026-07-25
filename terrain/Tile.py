from main import Constants
from utils.Assets import loadImage
from view.Sprite import Sprite
from utils.Vectors import Vec3

class Tile(Sprite):
    def __init__(self, image_path, x, y):
        Sprite.__init__(self, loadImage(image_path))
        self.image_path = image_path
        self.x = x
        self.y = y
        self.location = Vec3(x, y, 0)
        self.objects = []
        self.layer = Constants.GROUND_LAYER

    def __str__(self):
        return "Tile " + str(self.x) + " " + str(self.y)

    def addObject(self, object):
        self.objects.append(object)

    def removeObject(self, object):
        self.objects.remove(object)

    def containsObject(self, type):
        for object in self.objects:
            if isinstance(object, type):
                return True
        return False

    def getObject(self, type):
        for object in self.objects:
            if isinstance(object, type):
                return object
        return None