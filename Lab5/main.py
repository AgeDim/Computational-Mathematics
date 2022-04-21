import numpy as np
from Lab5.data import getdata_input
from Lab5.graphics import draw
from Lab5.method import euler_method


def main():
    print("\tЧисленное дифференцирование")
    data = getdata_input()
    answer = euler_method(data['f'], data['a'], data['b'], data['y0'], data['h'])

    if answer is None:
        print("\n\nВо время вычисления произошла ошибка!")
    else:
        x = np.array([dot[0] for dot in answer])
        y = np.array([dot[1] for dot in answer])
        acc_x = np.linspace(np.min(x), np.max(x), 100)
        acc_y = [data['acc_f'](i) for i in acc_x]
        draw(x, y, acc_x, acc_y)

        print("\n\nРезультаты вычисления.")
        print("%12s%12s%12s" % ("x", "y", "acc_y"))
        for i in range(len(answer)):
            print("%12.4f%12.4f%12.4f" % (answer[i][0], answer[i][1], data['acc_f'](answer[i][0])))

    input("\n\nНажмите Enter, чтобы выйти.")


main()
