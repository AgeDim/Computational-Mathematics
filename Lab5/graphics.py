from matplotlib import pyplot as plt


def draw(x, y, acc_x, acc_y):
    """ Отрисовать графики точного и численного решений """
    # Настраиваем всплывающее окно
    # plt.rcParams['toolbar'] = 'None'
    plt.gcf().canvas.set_window_title("График")

    # Настриваем оси
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker=">", ms=5, color='k',
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker="^", ms=5, color='k',
            transform=ax.get_xaxis_transform(), clip_on=False)

    # Отрисовываем график
    plt.plot(x, y, label="y(x)")
    plt.plot(acc_x, acc_y, label="acc_y(x)")

    plt.legend()
    plt.show(block=False)
