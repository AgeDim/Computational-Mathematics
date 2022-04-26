import math
import sys


class Data:

    def __init__(self, functionType):
        self.functionType = functionType

    def getFunction(self, x, order):
        match self.functionType:
            case 1:
                return self.getFirstFunction(x, order)
            case 2:
                return self.getSecondFunction(x, order)
            case 3:
                return self.getThirdFunction(x, order)
            case 4:
                return self.getFourthFunction(x, order)
            case _:
                return 0

    @staticmethod
    def getFirstFunction(x, order):
        return 2 * x - 3

    @staticmethod
    def getSecondFunction(x, order):
        return pow(x, 2) - x - 6

    @staticmethod
    def getThirdFunction(x, order):
        if x < 0:
            print(
                "Ну как так то! Вы же знаете что логарифм не может принимать отрицательные значения. Не нужно ломать мою прогу.")
            sys.exit(-228)
        return math.log(x, 2)

    @staticmethod
    def getFourthFunction(x, order):
        return 3 * math.cos(x / 2)

    def setFunctionType(self, functionType):
        self.functionType = functionType

    def getFunctionType(self):
        return self.functionType
