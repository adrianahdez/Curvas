### bspline.py ###

from __future__ import division

import math


def bspline(points, m):
    '''
        points - control points
        m - degree of B-splines
    '''
    M = len(points) - 1
    n = M - m + 1
    knots = [0] * m + [k / n for k in xrange(n + 1)] + [1] * m
    print knots
    
    def curve(t):
        if t == 1:
            return points[-1]

        k = m + int(math.floor(t * n))
        # values of N[m, k-m],...,N[m, k] at t
        Nk = [1] + [0] * m

        V = lambda m, i, t: (t - knots[i]) / (knots[i + m] - knots[i]) \
                            if knots[i] != knots[i + m] \
                            else 0

        for i in xrange(1, m + 1):
            for j in xrange(i, -1, -1):
                # count N[i, k-j]
                if j:
                    Nk[j] = Nk[j - 1] * (1 - V(i, k - j + 1, t)) + Nk[j] * V(i, k - j, t)
                else:
                    Nk[j] = Nk[j] * V(i, k - j, t)

        Nk.reverse()

        return [sum(p[j] * N for p, N in zip(points[k-m:k+1], Nk)) for j in (0, 1)]

    return curve


if __name__ == '__main__':
    import matplotlib.pyplot as plt
##    import numpy as np
  #el minimo numero de puntos de una bslpline3 son 4
    control_points = ((2, 3), (0, 0), (3, 3), (4, 1))#, (6, 3))    
    #control_points = ((2, 3), (0, 0),(3, 3), (4, 1), (6, 3),(5,4),(10,4),(10.,5))
##    control_points2=np.array(control_points)
    degree = 3
##    plt.plot(control_points2[:,0],control_points2[:,1],'ko')
    curve = bspline(control_points, degree)
    print "HOLA"

    N = 40
    points = map(curve, (i / N for i in xrange(N + 1)))
    print "points=",points
    x, y = ([p[j] for p in points] for j in (0, 1))
    plt.plot(x, y,'r-',lw=2)

    x, y = ([p[j] for p in control_points] for j in (0, 1))
    print "x= ",x
    print "y= ",y
    plt.plot(x, y,'b:o',lw=2)

    plt.grid(True)
    plt.axis([min(x)-0.1,max(x)+0.1, min(y)-0.1, max(y)+0.1])
    plt.show()
