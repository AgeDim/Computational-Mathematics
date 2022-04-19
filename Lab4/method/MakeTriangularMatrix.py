import sys


def makeTriangularMatrix(a, size):
    try:
        for k in range(size - 1):
            im = k
            for i in range(k + 1, size):
                if abs(a[im][k]) < abs(a[i][k]):
                    im = i
            if im != k:
                for j in range(size):
                    v = a[im][j]
                    a[im][j] = a[k][j]
                    a[k][j] = v
            for i in range(k + 1, size):
                v = 1.0 * a[i][k] / a[k][k]
                a[i][k] = 0
                if v != 0:
                    for j in range(k + 1, size):
                        a[i][j] = a[i][j] - v * a[k][j]
        return a
    except ZeroDivisionError as ex:
        print(ex)
        sys.exit(0)
