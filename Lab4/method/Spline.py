class Spline:

    def __init__(self, a, b, c, d, xi):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.xi = xi

    def getA(self):
        return self.a

    def getXi(self):
        return self.xi

    def getF(self, x, i):
        return float(self.a[i]) + float(self.b[i]) * (x - float(self.xi[i])) + float(self.c[i]) * (
                    x - float(self.xi[i])) * (x - float(self.xi[i])) + float(self.d[
                                                                                 i]) * (x - float(self.xi[i])) * (
                           x - float(self.xi[i])) * (x - float(self.xi[i]))
