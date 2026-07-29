from utils.Vectors import Vec3
from utils.mathutils import mapValue


class Segment:

    def __init__(self, start: Vec3, end: Vec3) -> None:
        self.start = start
        self.end = end

    def lerp(self, t: float) -> Vec3:
        x = mapValue(t, 0, 1, self.start.x, self.end.x)
        y = mapValue(t, 0, 1, self.start.y, self.end.y)
        z = mapValue(t, 0, 1, self.start.z, self.end.z)
        return Vec3(x, y, z)


