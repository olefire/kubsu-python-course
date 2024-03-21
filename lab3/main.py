from lab3.Pentagon import Pentagon
from lab3.Point import Point
from lab3.Triangle import Triangle

triangle: Triangle = Triangle(Point(3, 0), Point(0, 4), Point(0, 0))

pentagon: Pentagon = Pentagon([Point(1, 3), Point(1, 5), Point(3, 5), Point(4, 4), Point(3, 3)])

triangle.move(1, 2)
for point in triangle.points:
    print(point.x, point.y)

print(pentagon.square())
