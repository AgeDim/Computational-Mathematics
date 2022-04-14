from trapezoidalMethod import trapezoidal_method
from data import Data

def getdata_input():
    """ Получить данные с клавиатуры """
    print("\nВыберите функцию.")
    print(" 1 — x^2")
    print(" 2 — sin(x) / x")
    print(" 3 — x/(x-2)")
    while True:
        try:
            func_id = float(input("Функция: "))
            if not(func_id in range(1, 4)):
                raise AttributeError
            break
        except AttributeError:
            print("Функции нет в списке.")

    print("\nВведите пределы интегрирования.")
    while True:
        try:
            a, b = map(float, input("Пределы интегрирования: ").split())
            if a > b:
                a, b = b, a
            break
        except ValueError:
            print("Пределы интегрирования должны быть числами, введенными через пробел.")

    print("\nВведите погрешность вычисления.")
    while True:
        try:
            error = float(input("Погрешность вычисления: "))
            if error <= 0:
                raise ArithmeticError
            break
        except (ValueError, ArithmeticError):
            print("Погрешность вычисления должна быть положительным числом.")

    return a, b, func_id, error



print("\tЛабораторная работа #3")
print("\t Численное интегрирование")

a, b, func, epsilon = getdata_input()
data = Data(a, b, func, epsilon)
answer = trapezoidal_method(data)

print("\n\nРезультаты вычисления.")
print(f"Значение интеграла: {answer}")



