from Lab5.func import gettask


def getdata_input():
    """ Получить данные с клавиатуры """
    data = {}
    print("\nВыберите задачу.")
    print(" 1 — y' = y + (1 + x)y²\n     на [1; 1,5] при y(1) = -1")
    print(" 2 - y' = x² - 2y\n     на [0; 1] при y(0) = 1")
    while True:
        try:
            task_id = input("Задача: ")
            func, acc_func, a, b, y0 = gettask(task_id)
            if func is None:
                raise AttributeError
            break
        except AttributeError:
            print("Функции нет в списке!")
    data['f'] = func
    data['acc_f'] = acc_func
    data['a'] = a
    data['b'] = b
    data['y0'] = y0

    print("\nВведите шаг точек.")
    while True:
        try:
            h = float(input("Шаг точек: "))
            if h <= 0:
                raise ArithmeticError
            break
        except (ValueError, ArithmeticError):
            print("Шаг точек должен быть положительным числом.")
    data['h'] = h

    return data
