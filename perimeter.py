def square_area(side: float) -> float:
    """Периметр квадрата"""

    if side > 0: return side * 4

    return "Стороны должны быть больше нуля"

def rectangle_area(height: float, width: float):
    """Периметр прямоугольника"""

    if height > 0 and width > 0: return 2 * (height + width)

    return "Стороны должны быть больше нуля"

def cirkle_area(radius: float):
    """Периметр круга"""

    import math as m
    if radius > 0: return 2 * m.pi * radius

    return "Радиус должен быть больше нуля"
