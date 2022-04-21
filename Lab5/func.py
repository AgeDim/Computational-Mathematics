import sys
from math import exp


def gettask(task_id):
    """ Получить выбранную функцию """
    print("\nВведите интервал дифференцирования.")
    while True:
        try:
            a, b = map(float, input("Интервал дифференцирования: ").split())
            if a > b:
                a, b = b, a
            break
        except ValueError:
            print("Интервал дифференцирования должен быть числами, введенными через пробел.")
    print("\nВведите значение y.")
    while True:
        try:
            temp = float(input("Значение y: "))
            break
        except (ValueError, ArithmeticError):
            print("Y должен быть чилом!")
    if task_id == '1':
        if a == 0 or b == 0:
            print("К сожалению делить на ноль нельзя. Знаю печалька, но по другому никак)")
            sys.exit(1)
        return lambda x, y: y + (1 + x) * pow(y, 2), \
               lambda x: -1 / x, \
               a, \
               b, \
               temp
    elif task_id == '2':
        return lambda x, y: pow(x, 2) - 2 * y, \
               lambda x: 0.75 * exp(-2 * x) + 0.5 * pow(x, 2) - 0.5 * x + 0.25, \
               a, \
               b, \
               temp
    else:
        return None
