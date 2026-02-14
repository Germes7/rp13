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
    """Площадь круга"""

    import math as m
    if radius > 0: return m.pi * radius ** 2

    return "Радиус должен быть больше нуля"

from perimeter import *

Flag = True

while Flag:

    choice = int(input("Что вы хотите посчитать: 1 -квадрат, 2 - прямоугольник, 3 -круг >"))

    if choice == 1:
        side = float(input("Введите сторону квадрата >"))

        print(f"Площадь квадрата: {square_area(side)}")
        print(f"Периметр квадрата: {square_perimeter(side)}")

    elif choice == 2:
        height = float(input("Введите высоту прямоугольника >"))
        width = float(input("Введите ширину прямоугольника >"))

        print(f"Площадь прямоугольника: {rectangle_area(height, width)}")
        print(f"Периметр прямоугольника: {rectangle_perimeter(height, width)}")

    elif choice == 3:
        radius = float(input("Введите радиус круга >"))

        print(f"Площадь круга: {cirkle_area(radius)}")
        print(f"Периметр круга: {cirkle_perineter(radius)}")

    question = int(input("Продолжить -4, Выйти -5 >"))

    if question == 5:
        Flag = False