from typing import List

from lab3.Figure import Figure
from lab3.Point import Point


class Pentagon(Figure):
    def __init__(self, points: List[Point]):
        if len(points) != 5:
            raise ValueError("You need 5 points to form a pentagon.")
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    if ((points[k].x - points[i].x)*(points[j].y - points[i].y)
                            == (points[k].y - points[i].y)*(points[j].x - points[i].x)):
                        raise ValueError("Invalid Pentagon")
        super().__init__(points)

    def square(self) -> float:
        a, b, c, d, e = self.points
        s = abs((a.x - b.x) * (a.y + b.y) + (b.x - c.x) * (b.y + c.y) + (c.x - d.x) * (c.y + d.y)
                + (d.x - e.x) * (d.y + e.y) + (e.x - a.x) * (e.y + a.y)) / 2
        return s
