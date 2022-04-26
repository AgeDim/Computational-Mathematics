def getdata_input():
    """ Получить данные с клавиатуры """
    print("\nВыберите функцию.")
    print(" 1 — 2x - 3")
    print(" 2 — x^2 - x - 6")
    print(" 3 — log2(x) При x > 0")
    print(" 4 — 3 sin(x/2)")
    while True:
        try:
            func_id = float(input("Функция: "))
            if not(func_id in range(1, 5)):
                raise AttributeError
            break
        except AttributeError:
            print("Функции нет в списке!")
        except ValueError:
            print("Введенные данные должны быть числом")

    print("\nВведите количество точек.")
    while True:
        try:
            a = int(input("Количество точек: "))
            if a <= 1:
                raise AttributeError
            break
        except AttributeError:
            print("Количесво точек должно быть больше 1!")
        except ValueError:
            print("Введенные данные должны быть числом")
    x = [0] * a
    for i in range(0, a):
        x[i] = input(f"Введите {i+1} точку ")
    return func_id, x