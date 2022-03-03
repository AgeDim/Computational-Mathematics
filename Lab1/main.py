import sys


def determinant(a):
    n = len(a[0])
    det = 1
    for j in range(n):
        det *= a[j][j]
    return det


def divide_row(a, b, divider):
    for i in range(row):
        a[i] = a[i] / divider
    b = b / divider
    return a, b


def triangle_matrix(a, b):
    try:
        for k in range(row):
            for i in range(k + 1, row):
                if a[k][k] == 0:
                    raise ZeroDivisionError("Значение числа на главной диагонали при трансформации равно нулю!")
                mu = a[i][k] / a[k][k]
                for j in range(k, row):
                    temp = a[k][k] * float(mu)
                    a[i][j] = float("{0:.1f}".format(a[i][j])) - float("{0:.1f}".format(temp))
                b[0][k] -= (b[0][k] * float(mu))
        return a, b
    except ZeroDivisionError as ex:
        print(ex)
        sys.exit(0)


def result(a, b, deter):
    temp = 0
    x = [0] * row
    if deter == 0:
        print("Определитель матрицы равен 0, решений системы уравнений нет!")
        sys.exit(0)
    for i in range(row - 1, -1, -1):
        a[i], b[0][i] = divide_row(a[i], b[0][i], a[i][i])
    x[-1] = b[0][-1]
    for i in range(row-2, -1, -1):
        for j in range(row-1, i-1, -1):
            temp += x[j] * a[i][j]
        x[i] = b[0][i] - temp
        temp = 0
    return x


def deltas(a, b, x):
    temp = 0
    delta = [0] * row
    for i in range(row):
        for j in range(row):
            temp += a[i][j] * x[j]
        delta[i] = abs(float("{0:.30f}".format(b[0][i] - temp)))
    return delta


print("Введите число 1 для ввода матрицы из консоли или число 2 для ввода матрицы из файла!")
try:
    indecator = int(input())
    if indecator != 1 and indecator != 2:
        raise IndexError("Неверный аргумент!")
except IndexError as e:
    print(e)
    sys.exit()
except ValueError:
    print("Неверный аргумент")
    sys.exit(0)
print("Введите размерность матрицы(Пример: 10 10).")
try:
    row, column = input().split()
    row = int(row)
    column = int(column)
    if row > 20:
        raise IndexError("Размер матрицы должен быть в диапазоне от 2 до 20")
    if row < 3:
        raise IndexError("Размер матрицы должен быть в диапазоне от 2 до 20")
    if column < 3:
        raise IndexError("Размер матрицы должен быть в диапазоне от 2 до 20")
    if column > 20:
        raise IndexError("Размер матрицы должен быть в диапазоне от 2 до 20")
except ValueError:
    print("Неверные аргументы")
    sys.exit(0)
except IndexError as e:
    print(e)
    sys.exit(0)

try:
    if indecator == 1:
        print("введите матрицу коэфициентов (по строках, пробелы между коэффициентами")
        matrix = [list(map(float, (input(f"строка {i + 1}: ").split()))) for i in range(row)]
        print("введите правую часть матрицы")
        coef_of_matr = [list(map(float, (input().split())))]
        for i in range(row):
            if len(matrix[i]) != row or len(coef_of_matr[0]) != row:
                raise IndexError("Неверное количество элементов")
        print("Матрица")
        for i in range(row):
            print(matrix[i], coef_of_matr[0][i])
        matrix, coef_of_matr = triangle_matrix(matrix, coef_of_matr)
        print("Треугольная матрица имеет вид")
        for i in range(row):
            print(matrix[i], coef_of_matr[0][i])
        det = determinant(matrix)
        print("det= {:.15f}".format(det))
        print("Корни системы уравнений:")
        x = result(matrix, coef_of_matr, det)
        for i in range(row):
            print(x[i])
        print("Невязки:")
        print(deltas(matrix, coef_of_matr, x))
except ValueError:
    print("Неверные аргументы")
    sys.exit(0)
except IndexError as e:
    print(e)
    sys.exit(0)

if indecator == 2:
    print(r"Введите путь к файлу(Пример:C:\matrix.txt)")
    path = input()
    try:
        f = open(path, 'r')
        matrix_in_file = [list(map(float, f.readline().split(" "))) for i in range(row)]
        coef_of_file_matrix = [list(map(float, f.readline().split()))]
        for i in range(row):
            if len(matrix_in_file[i]) != row or len(coef_of_file_matrix[0]) != row:
                raise IndexError("Неверное количество элементов")
        print("Матрица")
        for i in range(row):
            print(matrix_in_file[i], coef_of_file_matrix[0][i])
        matrix_in_file, coef_of_file_matrix = triangle_matrix(matrix_in_file, coef_of_file_matrix)
        print("Треугольная матрица имеет вид")
        for i in range(row):
            print(matrix_in_file[i], coef_of_file_matrix[0][i])
        print("det= {:.15f}".format(determinant(matrix_in_file)))
        det = determinant(matrix_in_file)
        print("Корни системы уравнений:")
        x = result(matrix_in_file, coef_of_file_matrix, det)
        for i in range(row):
            print(x[i])
        print("Невязки:")
        print(deltas(matrix_in_file, coef_of_file_matrix, x))
    except FileNotFoundError:
        print("Файл не найден!")
    except ValueError:
        print("Неверные аргументы")
        sys.exit(0)
    except IndexError as e:
        print(e)
        sys.exit(0)
