import math
import sys
from data import Data

def trapezoidal_method(data):
    prevResult = 0
    result = 4.9E-324 + 2
    error = 4.9E-324
    n = 2
    while abs((result - prevResult)) > Data.getEpsilon(data):
        prevResult = result
        result = 0
        step = (Data.getUpperBound(data) - Data.getLowerBound(data)) / n
        for i in range(n):
            leftY = Data.getFunction(data, Data.getLowerBound(data) + step * i, 0)
            rightY = Data.getFunction(data, Data.getLowerBound(data) + step * (i+1), 0)
            isNormalLeftY = math.isfinite(leftY)
            isNormalRightY = math.isfinite(rightY)
            if not isNormalRightY:
                temp = Data.getFunction(data, Data.getLowerBound(data) + step * (i + 1), 2)
                if temp > error:
                    error = temp
            else:
                if not isNormalLeftY:
                    temp = Data.getFunction(data, Data.getLowerBound(data) + step * i, 2)
                    if temp > error:
                        error = temp
                else:
                    result = result + leftY + rightY
        result *= (step / 2)
        n += 2
    try:
        if abs(error) > abs(result):
            raise ArithmeticError("Коэффициент R больше, чем полученный результат. Возможно, интеграл расходится.")
    except ArithmeticError as e:
        print(e)
        sys.exit(0)
    return result
