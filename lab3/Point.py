import math


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def dist(self, other: object) -> float:
        if not isinstance(other, Point):
            raise TypeError("other must be Point")
        return math.sqrt((self.get_x() - other.get_x()) ** 2 + (self.get_y() - other.get_y()) ** 2)