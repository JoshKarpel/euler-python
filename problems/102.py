import os

def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.quadrant = self.get_quadrant()
        self.tilted_quadrant = self.get_tilted_quadrant()

    def get_quadrant(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x > 0 and self.y < 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x < 0 and self.y > 0:
            return 4

    def get_tilted_quadrant(self):
        if self.y > self.x and self.y > -self.x:
            return 1
        elif self.y < self.x and self.y > -self.x:
            return 2
        elif self.y < self.x and self.y < -self.x:
            return 3
        elif self.y > self.x and self.y < - self.x:
            return 4


class Triangle:
    def __init__(self, points):
        self.points = points
        self.a = points[0]
        self.b = points[1]
        self.c = points[2]
        self.quadrants = [p.quadrant for p in points]

    def legal(self):
        # if self.a.quadrant == self.b.quadrant == self.c.quadrant:  # if all in same quadrant, not as general as "side check" below
        #     return False
        if sign(self.a.x) == sign(self.b.x) == sign(self.c.x) or sign(self.a.y) == sign(self.b.y) == sign(self.c.y):  # if all to "one side" of plane
            return False
        elif self.a.tilted_quadrant == self.b.tilted_quadrant or self.b.tilted_quadrant == self.c.tilted_quadrant or self.c.tilted_quadrant == self.a.tilted_quadrant:
            return False
        else:
            return True


def solve():
    filepath = os.path.join(os.path.dirname(__file__), '102_triangles.txt')
    with open(filepath) as file:
        raw_triangles = [[int(x) for x in line.strip('\n').split(',')] for line in file]

    triangles = []
    for raw_triangle in raw_triangles:
        triangles.append(Triangle([Point(raw_triangle[0], raw_triangle[1]), Point(raw_triangle[2], raw_triangle[3]), Point(raw_triangle[4], raw_triangle[5])]))

    return len([triangle for triangle in triangles if triangle.legal()])


if __name__ == '__main__':
    print(solve())
