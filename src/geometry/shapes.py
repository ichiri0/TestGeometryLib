import math


class Geometry:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = sorted([side1, side2, side3])
        return sides[0]**2 + sides[1]**2 == sides[2]**2

    @staticmethod
    def calculate_area_generic(shape):
        return shape.calculate_area()


class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) *
                         (s - self.side2) * (s - self.side3))
        return area
