from src.geometry.shapes import Geometry, Circle, Triangle


circle = Circle(2)
triangle = Triangle(3, 4, 5)

# Площадь круга
print(Geometry.calculate_area_generic(circle))

# Площадь треугольника
print(Geometry.calculate_area_generic(triangle))
