import matplotlib.pyplot as plt
import numpy as np

#funcion recurvisa
def B(coorArr, i, j, t):
    if j == 0:
        return coorArr[i]
    return B(coorArr, i, j - 1, t) * (1 - t) + B(coorArr, i + 1, j - 1, t) * t

P=np.array([[0., 0.5],[0.2, 1.],[1., -0.8],[1.2,0.6]])  
##n=4
x=P[:,0]
y=P[:,1]
n=x.size
fig=plt.figure(1)


##plt.text(-0.06, 0.5, 'P0')
##plt.text(0.15, 1.01, 'P1')
##plt.text(1.05, 0.8, 'P2')
##plt.text(1.15, 0.57, 'P3')

xb=[]
yb=[]
for t in np.linspace(0.,1.,25):
    a = B(x, 0, n - 1, t)
    b = B(y, 0, n - 1, t)
    xb.append(a)
    yb.append(b)
plt.plot(xb,yb,'go')

plt.plot(x,y,'r-',x,y,'ko',ms=8)

plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.axis([min(x)-0.065,max(x)+.05,min(y)-0.05,max(y)+0.05])
plt.show()