def square_perimeter(side: float) -> float:
    """Периметр квадрата"""

    if side > 0: return side * 4

    return "Стороны должны быть больше нуля"

def rectangle_perimeter(height: float, width: float):
    """Периметр прямоугольника"""

    if height > 0 and width > 0: return 2 * (height + width)

    return "Стороны должны быть больше нуля"


