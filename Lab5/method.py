def euler_method(f, a, b, y0, h):
    """ Метод Эйлера """
    dots = [(a, y0)]
    n = int((b - a) / h)

    for i in range(1, n + 1):
        dots.append((dots[i - 1][0] + h,
                     dots[i - 1][1] + h * f(dots[i - 1][0], dots[i - 1][1])))
    return dots
