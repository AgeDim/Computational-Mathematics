import math


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
        if order == 0:
            return 1 / x
        else:
            return 2 / pow(x, 3)

    @staticmethod
    def getThirdFunction(x, order):
        exp = math.exp(pow(x, 2) - x)
        if order == 0:
            return 3 * exp
        else:
            return (2 * x - 1) * (6 * x - 3) * exp + 6 * exp

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
