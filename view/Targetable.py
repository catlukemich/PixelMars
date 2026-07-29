import pygame

from VDebugger.vdebugger import vd
from utils.Segment import Segment
from utils.Vectors import Vec3
from view.Sprite import Sprite
from view.View import View


class Targetable:
    """Targetable is type of component that allows targeting by lerping toward an object, use in composition with sprites"""

    def __init__(self, view : View, sprite: Sprite) -> None:
        self.t = 0
        self.segment = Segment(view.center, sprite.location)
        self.location = Vec3(view.center.x, view.center.y, view.center.z)
        self.has_finished = False

    def update(self, clock: pygame.time.Clock):
        self.t += 0.05
        self.location = self.segment.lerp(self.t)
        # vd("x, y, z", f"{self.location.x} {self.location.y} {self.location.z}")
        if self.t > 1:
            self.t = 1
            self.has_finished = True

    def hasFinished(self):
        return self.has_finished

    def getLocation(self):
        return self.location