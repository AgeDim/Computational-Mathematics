import getData
from Lab4.method.MethodSpline import MethodSpline
from data import Data
from graphics import drawingFunction

func, x = getData.getdata_input()

data = Data(func)
y = [0] * len(x)
for i in range(len(x)):
    y[i] = data.getFunction(float(x[i]), 0)

methodSpline = MethodSpline(x, y, len(x))
spline = methodSpline.getSpline()
drawingFunction(data, spline, x, y)