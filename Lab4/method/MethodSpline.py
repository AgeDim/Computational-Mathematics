from Spline import Spline
from MakeTriangularMatrix import makeTriangularMatrix
from ResultRoot import getResult
class MethodSpline:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

    def getSpline(self):
        h = self.makeH(self.x)
        argC = self.makeC(h, self.y)
        argC = makeTriangularMatrix(argC, self.n)
        c = getResult(argC, self.n)
        b = self.makeB(h, c)
        d = self.makeD(h, c)
        return Spline(self.y, b, c, d, self.x)

    def makeH(self, argX):
        resH = [0] * (len(argX) - 1)
        for i in range(len(resH)):
            resH[i] = argX[i + 1] - argX[i]
        return resH

    def makeC(self, argH, argY):
        argC = [[0 for j in range(len(argY))] for i in range(len(argY) + 1)]
        for i in range(len(argY)):
            for j in range(len(argY) + 1):
                argC[i][j] = 0.0
        argC[0][0] = 1.0
        argC[0][len(argH) + 1] = 0
        argC[len(argH)][len(argH)] = 1
        argC[len(argH)][len(argH) + 1] = 0
        for i in range(len(argY) - 1):
            argC[i][i - 1] = argH[i - 1]
            argC[i][i] = ((argH[i] + argH[i - 1]) * 2)
            argC[i][i + 1] = argH[i]
            argC[i][len(argH) + 1] = 6 * (((argY[i + 1] - argY[i]) / argH[i]) - ((argY[i] - argY[i - 1]) / argH[i - 1]))
        return argC

    def makeB(self, h, c):
        b = [] * len(self.y)
        b[0] = 0
        for i in range(1, len(b)):
            b[i] = (self.y[i] - self.y[i - 1]) / h[i - 1] + h[i - 1] * (2 * c[i] / 3 + 2 * c[i - 1] / 6)
        return b

    def makeD(self, h, c):
        d = [] * len(self.y)
        d[0] = 0
        for i in range(1, len(d)):
            d[i] = (c[i] - c[i - 1]) / (h[i - 1] * 3)
        return d
