def sum_numbers(a: float, b: float) -> float:
    return a + b


def multi_number (a: float, b: float) ->float:
    return a * b

def factorial(n: int) ->int:
    """Функция вычисления факториала числа"""

    if n == 0:
        return "Ошибка"
    mult = 1
    for i in range(1, n + 1):
        mult *= i

    return mult

def average_3(a: float, b: float, c: float) -> float:

    return (a + b + c) / 3

def Hello():
    return "Hello"

def square_area(side: float) -> float:
    """Площадь квадрата"""

    if side > 0: return side ** 2

    return "Стороны должны быть больше нуля"

def rectangle_area(height: float, width: float):
    """Площадь прямоугольника"""

    if height > 0 and width > 0: return height * width

    return "Стороны должны быть больше нуля"


def cirkle_area(radius: float):
    pass