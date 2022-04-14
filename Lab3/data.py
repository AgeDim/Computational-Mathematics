import math
import sys


class Data:

    def __init__(self, upperBound, lowerBound, functionType, epsilon):
        self.upperBound = upperBound
        self.lowerBound = lowerBound
        self.functionType = functionType
        self.epsilon = epsilon

    def getFunction(self, x, order):
        match self.functionType:
            case 1:
                return self.getFirstFunction(x, order)
            case 2:
                return self.getSecondFunction(x, order)
            case 3:
                return self.getThirdFunction(x, order)
            case _:
                return 0

    @staticmethod
    def getFirstFunction(x, order):
        if order == 0:
            return pow(x, 2)
        else:
            return 2

    @staticmethod
    def getSecondFunction(x, order):
        if x == 0:
            return math.inf
        if order == 0:
            return math.sin(x) / x
        else:
            return (-math.sin(x) - ((2 * math.cos(x)) / x) + ((2 * math.sin(x)) / pow(x, 2))) / x

    @staticmethod
    def getThirdFunction(x, order):
        if x == 2:
            print(f"Разрыв второго рода в точке x={x}")
            sys.exit(1)
        if order == 0:
            return x / (x - 2)
        else:
            return (2 * ((x / (x - 2)) - 1)) / (pow(x - 2, 2))

    def setEpsilon(self, epsilon):
        self.epsilon = epsilon

    def getEpsilon(self):
        return self.epsilon

    def setFunctionType(self, functionType):
        self.functionType = functionType

    def getFunctionType(self):
        return self.functionType

    def setUpperBound(self, upperBound):
        self.upperBound = upperBound

    def setLowerBound(self, lowerBound):
        self.lowerBound = lowerBound

    def getLowerBound(self):
        return self.lowerBound

    def getUpperBound(self):
        return self.upperBound
