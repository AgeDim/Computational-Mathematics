# Лабораторная работа №3
def trapezoid_method(f, a, b, e, min_n=4, max_itr=10):
    """ Метод трапеций """
    data = {}

    n = min_n
    result = float('inf')

    while n <= n * (2 ** max_itr):
        last_result = result
        result = (f(a) + f(b)) / 2

        h = (b - a) / n
        x = a + h

        for i in range(n - 1):
            result += f(x)
            x += h
        result *= h

        if abs(result - last_result) <= e:
            break
        else:
            n *= 2

    data['result'] = result
    data['n'] = n

    return data


def getfunc(func_id):
    """ Получить выбранную функцию """
    if func_id == '1':
        return lambda x: x ** 2
    elif func_id == '2':
        return lambda x: 1 / x
    elif func_id == '3':
        return lambda x: x ** 3 - 3 * (x ** 2) + 6 * x - 19
    else:
        return None


def getdata_input():
    """ Получить данные с клавиатуры """
    data = {}
    print("\nВыберите функцию.")
    print(" 1 — x²")
    print(" 2 — 1 / x")
    print(" 3 — x³ - 3x² + 6x - 19")
    while True:
        try:
            func_id = input("Функция: ")
            func = getfunc(func_id)
            if func is None:
                raise AttributeError
            break
        except AttributeError:
            print("Функции нет в списке.")
    data['func'] = func
    method = 'trapezoid_method'
    data['method'] = method

    print("\nВведите пределы интегрирования.")
    while True:
        try:
            a, b = map(float, input("Пределы интегрирования: ").split())
            if a > b:
                a, b = b, a
            break
        except ValueError:
            print("Пределы интегрирования должны быть числами, введенными через пробел.")
    data['a'] = a
    data['b'] = b

    print("\nВведите погрешность вычисления.")
    while True:
        try:
            error = float(input("Погрешность вычисления: "))
            if error <= 0:
                raise ArithmeticError
            break
        except (ValueError, ArithmeticError):
            print("Погрешность вычисления должна быть положительным числом.")
    data['error'] = error

    return data


def main():
    print("\tЛабораторная работа #3 (19)")
    print("\t Численное интегрирование")

    data = getdata_input()
    if data['method'] == 'trapezoid_method':
        answer = trapezoid_method(data['func'], data['a'], data['b'], data['error'])
    else:
        answer = None

    print("\n\nРезультаты вычисления.")
    print(f"Значение интеграла: {answer['result']}")
    print(f"Количество разбиений: {answer['n']}")


main()
