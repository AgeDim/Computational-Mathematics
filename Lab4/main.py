import getData
from data import Data

func, x = getData.getdata_input()

data = Data(func)
y = [0] * len(x)
for i in range(len(x)):
    y[i] = data.getFunction(float(x[i]), 0)
