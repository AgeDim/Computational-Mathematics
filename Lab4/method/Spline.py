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
        return self.a[i] + self.b[i] * (x - self.xi[i]) + self.c[i] * (x - self.xi[i]) * (x - self.xi[i]) + self.d[
            i] * (x - self.xi[i]) * (x - self.xi[i]) * (x - self.xi[i])
