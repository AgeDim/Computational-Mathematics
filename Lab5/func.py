from math import exp


def gettask(task_id):
    """ Получить выбранную функцию """
    if task_id == '1':
        return lambda x, y: y + (1 + x) * (y ** 2), \
               lambda x: -1 / x, \
               1, \
               1.5, \
               -1
    elif task_id == '2':
        return lambda x, y: (x ** 2) - 2 * y, \
               lambda x: 0.75 * exp(-2 * x) + 0.5 * (x ** 2) - 0.5 * x + 0.25, \
               0, \
               1, \
               1
    else:
        return None
