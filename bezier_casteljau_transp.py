import matplotlib.pyplot as plt
import numpy as np


# funcion recurvisa
def B(coorArr, i, j, t):
    if j == 0:
        return coorArr[i]
    return B(coorArr, i, j - 1, t) * (1 - t) + B(coorArr, i + 1, j - 1, t) * t

P = np.array([np.array([[2.5, 10.], [4., 12.], [6., 12.]]),
              np.array([[6., 12.], [8., 12.], [9., 10.]]),
              np.array([[9., 10.], [10., 8.], [10., 6.]]),
              np.array([[10., 6.], [8., 7.], [6., 7.]]),
              np.array([[6., 7.], [4., 7.], [2., 6.]]),
              np.array([[2., 6.], [0.8, 5.], [0.8, 4.]]),
              np.array([[0.8, 4.], [0.8, 3.], [1.7, 1.7], [2., 1.]]),
              np.array([[2., 1.], [3., 0.5], [5., 0.8], [6., 1.]]),
              np.array([[6., 1.], [7., 1.4], [9., 2.], [10., 3.]]),
              np.array([[10., 6.], [10., 3.]]),
              np.array([[10., 3.], [10., 1.], [13.5, 1.]])])

print(P)

fig = plt.figure(1)

xb = []
yb = []

xMax = 0
xMin = 0
yMax = 0
yMin = 0

for pt in P:
    x = pt[:, 0]
    y = pt[:, 1]
    m = x.size
    # Coordinate system boundaries
    currentXMax = max(x)
    currentYMax = max(y)
    currentXMin = min(x)
    currentYMin = min(y)

    if currentXMax > xMax:
        xMax = currentXMax

    if currentYMax > yMax:
        yMax = currentYMax

    if currentXMin < xMin:
        xMin = currentXMin

    if currentYMin < yMin:
        yMin = currentYMin

    for t in np.linspace(0., 1., 25):
        a = B(x, 0, m - 1, t)
        b = B(y, 0, m - 1, t)
        xb.append(a)
        yb.append(b)
    plt.plot(xb, yb, 'go', ms=2)

    plt.plot(x, y, 'r-', x, y, 'ko', ms=6)

plt.axis([xMin - 0.065, xMax + .5, yMin - 0.05, yMax + 0.5])

plt.show()
