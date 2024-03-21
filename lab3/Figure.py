from typing import List

from lab3.Point import Point


class Figure:
    def __init__(self, points: List[Point]):
        self.points = points

    def move(self, dx: float, dy: float):
        for point in self.points:
            point.move(dx, dy)

    def square(self) -> float:
        raise Exception("Method is not overridden")

    def compare(self, o: object) -> int:
        if not isinstance(o, Figure):
            raise TypeError("Object must be figure")

        self_square = self.square()
        other_square = o.square()

        if self_square == other_square:
            return 0
        if self_square > other_square:
            return 1
        return -1
