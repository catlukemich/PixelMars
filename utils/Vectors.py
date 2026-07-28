import math


class Vec2:
    def __init__(self, x: float = 0, y: float = 0):
        self.x: float = x
        self.y: float = y


class Vec3:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vec3(self.x, self.y, self.z)
        result.x += other.x
        result.y += other.y
        result.z += other.z
        return result

    def __sub__(self, other):
        result = Vec3(self.x, self.y, self.z)
        result.x -= other.x
        result.y -= other.y
        result.z -= other.z
        return result

    def __mul__(self, val):
        result = Vec3(self.x, self.y, self.z)
        result.x *= val
        result.y *= val
        result.z *= val
        return result

    def __truediv__(self, val):
        result = Vec3(self.x, self.y, self.z)
        result.x /= val
        result.y /= val
        result.z /= val
        return result

    # Counterclockwise rotation, when angle is positive.
    def rotate(self, angle):
        rads = math.radians(-angle)
        x = self.x * math.cos(rads) - self.y * math.sin(rads)
        y = self.x * math.sin(rads) + self.y * math.cos(rads)
        self.x = x
        self.y = y
        return self

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        dist = math.sqrt(dx**2 + dy**2 + dz**2)
        return dist
