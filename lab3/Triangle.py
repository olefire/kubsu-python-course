import math

from lab3.Figure import Figure
from lab3.Point import Point


class Triangle(Figure):
    def __init__(self, a: Point, b: Point, c: Point):
        if not (a.dist(b) + b.dist(c) > a.dist(c) and
                a.dist(b) + a.dist(c) > b.dist(c) and
                b.dist(c) + a.dist(c) > a.dist(b)):
            raise ValueError("Invalid triangle")
        super().__init__([a, b, c])

    def square(self):
        x, y, z = self.points
        a = x.dist(y)
        b = x.dist(z)
        c = y.dist(z)
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
