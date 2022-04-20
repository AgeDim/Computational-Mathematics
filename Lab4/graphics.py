from matplotlib import pyplot as plt


def drawingFunction(data, splines, xf, yf):
    xData = [0.] * 10000
    yData = [0.] * 10000
    yData2 = [0.] * 10000

    step = (float(splines.getXi()[len(splines.getXi()) - 1]) - float(splines.getXi()[0])) / 1000
    x = float(splines.getXi()[0]) - 0.1
    xData[0] = x
    yData[0] = float(splines.getF(x, 0))
    yData2[0] = data.getFunction(float(x), 0)
    courantX = float(splines.getXi()[0])
    k = 0
    i = 0
    while x < float(splines.getXi()[len(splines.getXi()) - 1]):
        i += 1
        x += step
        if x > float(courantX) and k < len(splines.getXi()) - 1:
            k += 1
            courantX = splines.getXi()[k]
        xData[i] = x
        yData[i] = splines.getF(x, k)
        yData2[i] = data.getFunction(float(x), 0)
    else:
        xData = xData[0:i]
        yData = yData[0:i]
        yData2 = yData2[0:i]
    plt.gcf().canvas.set_window_title("График")
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker=">", ms=5, color='k',
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker="^", ms=5, color='k',
            transform=ax.get_xaxis_transform(), clip_on=False)
    plt.plot(xData, yData, ':', linewidth=2)
    plt.plot(xData, yData2, linewidth=4)
    plt.grid(True)
    plt.show(block=False)
