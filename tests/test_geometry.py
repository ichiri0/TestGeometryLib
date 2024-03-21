import unittest, math
from src.geometry.shapes import Geometry

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(Geometry.circle_area(1), math.pi)
        self.assertAlmostEqual(Geometry.circle_area(0), 0)
        self.assertAlmostEqual(Geometry.circle_area(2.5), math.pi * 2.5 ** 2)

    def test_triangle_area(self):
        self.assertAlmostEqual(Geometry.triangle_area(3, 4, 5), 6)
        self.assertAlmostEqual(Geometry.triangle_area(5, 12, 13), 30)
        self.assertAlmostEqual(Geometry.triangle_area(7, 8, 9), 26.832815729997478)

    def test_is_right_triangle(self):
        self.assertTrue(Geometry.is_right_triangle(3, 4, 5))
        self.assertTrue(Geometry.is_right_triangle(5, 12, 13))
        self.assertFalse(Geometry.is_right_triangle(7, 8, 9))
