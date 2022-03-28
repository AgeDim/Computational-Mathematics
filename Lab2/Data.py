import math

def getThirdSystem(x1, x2, x3, dataType):
    if dataType == 0:
        return [pow(x1, 2) + pow(x2, 2) + pow(x3, 2) - 1, 2 * pow(x1, 2) + pow(x2, 2) - 4 * x3,3 * pow(x1, 2) - 4 * x2 + pow(x3, 2)]
    else:
        if dataType == 1:
            return [2 * x1, 2 * x2, 2 * x3]
        else:
            if dataType == 2:
                return [4 * x1, 2 * x2, -4]
            else:
                return [6 * x1, -4, 2 * x3]


def getSecondSystem(x1, x2, dataType):
    if dataType == 0:
        return [x1 + 3 * math.log10(x1) - pow(x2, 2), 2 * pow(x1, 2) - x1 * x2 - 5 * x1 + 1]
    else:
        if dataType == 1:
            return [1 + (3 * 0.43429 / x1), -2 * x2]
        else:
            return [4 * x1 - x2 - 5, -x1]


def getFirstSystem(x1, x2, dataType):
    if dataType == 0:
        return [pow(x1, 2) + pow(x2, 2) - 4, -3 * pow(x1, 2) + x2]
    else:
        if dataType == 1:
            return [2 * x1, 2 * x2]
        else:
            return [(-6 * x1), 1]


def getSystem(x, dataType, sysType):
    match sysType:
        case 1:
            return getFirstSystem(x[0], x[1], dataType)
        case 2:
            return getSecondSystem(x[0], x[1], dataType)
        case 3:
            return getThirdSystem(x[0], x[1], x[2], dataType)
        case _:
            return

