import copy
import sys
from math import log, cos, sin
import Data


def isNaN(x):
    return str(x) == str(1e400*0)


def half_del(a, b):
    """Метод делит интервал по полам"""
    return (a + b) / 2


def get_parameter():
    """Получить данные от пользователя"""
    a = float(input("Введите точку a :"))
    b = float(input("Введите точку b :"))
    e = float(input("Введите точность E:"))

    print(f'a = {a} \nb = {b} \nE = {e} ')
    return a, b, e


def half_interval(q, w, r, n):
    print("\033[32m \nМетод деления пополам\033[0m")
    counter = 0
    max_counter = 200
    while abs(w - q) > r:
        counter += 1
        if counter >= max_counter:
            print('Слишком много шагов')
            break
        if abs(w - q) <= r:
            print('Значение math.abs(b-a) стало меньше чем E')
            break
        print(f'\033[33m\n\nШаг №{counter}\033[0m')
        fa = func1(q, n)
        c = half_del(q, w)
        fc = func1(c, n)
        if fa * fc >= 0:
            q = c
        else:
            w = c
        print(f'f(a) = {fa} f(c) = {fc} f(a) * f(c) = {fa * fc}')
        print(f'a = {q} b = {w}')
        print(f'x={c}')


# функция
def func1(x, n):
    match n:
        case "1":
            return pow(x, 3) - x + 4
        case "2":
            return pow(x, 3) - 6 * pow(x, 2) + 3 * x + 11
        case "3":
            return log(abs(x), e) - 0.05 * pow(e, x)
        case "4":
            return
        case "5":
            return


# производная
def func1d(x, n):
    match n:
        case "1":
            return 3 * pow(x, 2) - 1
        case "2":
            return pow(x, 3) - x + 4
        case "3":
            return 1 / abs(x) - 0.05 * pow(e, x)
        case "4":
            return pow(x, 3) - x + 4
        case "5":
            return pow(x, 3) - x + 4


def method(q, w, r, n):
    counter = 0
    max_counter = 200
    x0 = (q + w) / 2
    xn = func1(x0, n)
    xn1 = xn - func1(xn, n) / func1d(xn, n)
    print("\033[32m\nМетод касательных\033[0m")
    while abs(xn1 - xn) > r:
        counter += 1
        if counter >= max_counter:
            print('Слишком много шагов')
            break
        if abs(w - q) <= r:
            print('Значение math.abs(b-a) стало меньше чем E')
            break
        print(f'\033[33m\n\nШаг №{counter}\033[0m')
        xn = x0
        xn1 = xn - func1(xn, n) / func1d(xn, n)
        x0 = xn1
        print(f'xn = {xn1} n={counter} f(x)={func1(xn1, n)} derivative={func1d(xn1, n)}')


def function1(x, y):
    return sin(x + y) - 1.2 * x


def function2(x, y):
    return x * x + y * y - 1


def func11(x, y):
    return cos(x + y) - 1.2


def func12(x, y):
    return cos(x + y)


def func21(x, y):
    return 2 * x


def func22(x, y):
    return 2 * y


def ober_matr(a):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    aa = a[0][0]
    a[0][0] = a[1][1] / det
    a[1][1] = aa / det
    aa = a[0][1]
    a[0][1] = -a[1][0] / det
    a[1][0] = -aa / det


def printSystemIteration(iteration, previous, current):
    printLines()
    print(f'Iteration:{iteration} | ')
    for i in range(len(previous)):
        print(f"x {i + 1}: {current[i]} | ")
        print(f"epsilon: {current[i] - previous[i]} | ")
    print('\n')


def printLines():
    print("========================================================")


def printSystems():
    print("Выберите систему для решения: ")
    print("1) x1^2 + x2^2 = 4")
    print("   x2 = 3*x1^2")
    print("2) x1 + 3*lg(x1) - x2^2 = 0")
    print("   2*x1^2 - x1*x2 - 5*x1 + 1 = 0")
    print("3) x1^2 + x2^2 + x3^2 = 1")
    print("   2*x1^2 + x1^2 - 4*x3^2 = 0")
    print("   3*x1^2 - 4*x2 + x3^2 = 0")

def solveWithNewtonMethod(solution, sysType, e):
    try:
        bol = False
        res = copy.deepcopy(solution)
        iteration = 0
        while True:
            if bol:
                break
            function = Data.getSystem(solution, 0, sysType)
            Jacobi = [[0] * len(solution)] * len(solution)
            for i in range(len(solution)):
                Jacobi[i] = Data.getSystem(solution, i + 1, sysType)
            JacobiCopy = copy.deepcopy(Jacobi)
            determinant = findDeterminant(JacobiCopy)
            reverseJacobi = reverseMatrix(Jacobi)
            rightPart = matrixMultiplication(reverseJacobi, function)
            for i in range(len(res)):
                res[i] = res[i] - (1 / determinant) * rightPart[i]
                if abs(float(res[i] - solution[i])) <= float(e):
                    bol = True
            iteration += 1
            printSystemIteration(iteration, solution, res)
            solution = copy.deepcopy(res)
            if iteration > 500:
                raise StopIteration("Слишком много итераций, попробуйте другие корни.")
        return res
    except StopIteration as e:
        print(e)


def matrixMultiplication(matrix1, matrix2):
    result = [0] * len(matrix2)
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            result[i] = result[i] + matrix1[i][j] * matrix2[j]
    return result


def reverseMatrix(matrix):
    result = [[0]*len(matrix)] * len(matrix)
    if len(matrix[0]) >= 3:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                result[i][j] = pow(-1, i + j) * findDeterminant(findMinor(matrix, i + 1, j + 1))
    else:
        result[0] = [matrix[1][1], (-1*matrix[0][1])]
        result[1] = [(-1*matrix[1][0]), matrix[0][0]]
    return result


def findMinor(matrix, row, column):
    result = [[0] * (len(matrix)-1)]* (len(matrix)-1)
    temp = [[0] * (len(matrix)-1)]* (len(matrix))
    isRow = False
    for i in range(len(matrix)):
        if i == row-1 and isRow == False:
            isRow = True
            continue
        if isRow:
            temp[i-1] = matrix[i]
        else:
            temp[i] = matrix[i]
    isRow = False
    c = 0
    for i in range(len(temp)):
        if i == row-1 and isRow == False:
            isRow = True
            continue
        if isRow:
            for j in range(len(temp)):
                if j != column - 1:
                    result[i-1][c] = matrix[i][j]
                    c = c+1
        else:
            for j in range(len(temp)):
                if j != column - 1:
                    result[i][c] = matrix[i][j]
                    c = c + 1
        c = 0
    return result



def findDeterminant(matrix):
    try:
        result = 1
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == j:
                    elementValidationAndModification(matrix, i, j)
                    rowSubtraction(matrix, i)
        for i in range(len(matrix)):
            result *= matrix[i][i]
        if result == 0:
            raise ValueError("Детерминант матрицы равен 0, введите другие значения")
        return result
    except ValueError as e:
        print(e)
        sys.exit(0)


def elementValidationAndModification(matrix, rowIndex, columnIndex):
    if matrix[rowIndex][columnIndex] == 0:
        columnSum = 0
        for i in range(len(matrix)):
            columnSum += matrix[i - 1][columnIndex]
        if columnSum == 0:
            raise ValueError("В матрице имеется нулевой столбец. Измените введенные даныне.")
        else:
            for i in range(rowIndex, len(matrix)):
                if matrix[i][columnIndex] != 0:
                    temp = matrix[rowIndex]
                    matrix[rowIndex] = matrix[i]
                    matrix[i] = temp
                    break


def rowSubtraction(matrix, elementIndex):
    for i in range(elementIndex + 1, len(matrix)):
        tempCoefficient = matrix[i][elementIndex] / matrix[elementIndex][elementIndex]
        for j in range(elementIndex, len(matrix)):
            matrix[i][j] = matrix[i][j] - matrix[elementIndex][j] * tempCoefficient
            if isNaN(matrix[i][j]):
                matrix[i][j] = 0


if __name__ == '__main__':
    print("Введите 1 или 2.")
    print("1 если вы хотите решить уравнения, 2 если вы хотите решить систему.")
    indecator = float(input())
    if indecator == 1:
        print("1. 3x^2 - 1")
        print("2. x^3 - 6x^2 + 3x + 11")
        print("3. ln(|x|) - 0.05e^x")
        print("4.")
        print("5.")
        print("Введите уравнение")
        n = input()
        a, b, e = get_parameter()
        half_interval(a, b, e, n)
        method(a, b, e, n)
    if indecator == 2:
        printSystems()
        index = float(input())
        temp = []
        print("Введите эпсилон")
        e = input()
        print("Введите корни системы")
        match index:
            case 3:
                temp.append(float(input("Введите корень первого уравнения")))
                temp.append(float(input("Введите корень второго уравнения")))
                temp.append(float(input("Введите корень третьего уравнения")))
            case _:
                temp.append(float(input("Введите корень первого уравнения")))
                temp.append(float(input("Введите корень второго уравнения")))
        solveWithNewtonMethod(temp, index, e)
