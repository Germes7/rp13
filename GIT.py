def sum_numbers(a: float, b: float) -> float:
    return a + b


print(sum_numbers(5, 7))

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

