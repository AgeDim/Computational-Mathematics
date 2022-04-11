from Lab3.io import getdata_input
from trapezoidalMethod import trapezoidal_method
from data import Data
print("\tЛабораторная работа #3")
print("\t Численное интегрирование")

a, b, func, epsilon = getdata_input()
data = Data(a, b, func, epsilon)
answer = trapezoidal_method(data)

print("\n\nРезультаты вычисления.")
print(f"Значение интеграла: {answer}")



