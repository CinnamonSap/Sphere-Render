import data
import utility


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) \
               and utility.epsilon_equal(self.y, other.y) \
               and utility.epsilon_equal(self.z, other.z)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) \
               and utility.epsilon_equal(self.y, other.y) \
               and utility.epsilon_equal(self.z, other.z)


class Ray:
    def __init__(self, pt, direction):
        self.pt = pt
        self.direction = direction

    def __eq__(self, other):
        return utility.epsilon_equal(self.pt.x, other.pt.x) \
               and utility.epsilon_equal(self.pt.y, other.pt.y) \
               and utility.epsilon_equal(self.pt.z, other.pt.z) \
               and utility.epsilon_equal(self.direction.x, other.direction.x) \
               and utility.epsilon_equal(self.direction.y, other.direction.y) \
               and utility.epsilon_equal(self.direction.z, other.direction.z)


class Sphere:
    def __init__(self, center, rad, color):
        self.center = center
        self.rad = rad
        self.color = color

    def __eq__(self, other):
        return utility.epsilon_equal(self.center.x, other.center.x) \
               and utility.epsilon_equal(self.center.y, other.center.y) \
               and utility.epsilon_equal(self.center.z, other.center.z) \
               and utility.epsilon_equal(self.rad, other.rad) \
               and utility.epsilon_equal(self.color, other.color)


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return utility.epsilon_equal(self.r, other.r) \
               and utility.epsilon_equal(self.g, other.g) \
               and utility.epsilon_equal(self.b, other.b)
