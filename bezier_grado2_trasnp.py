import matplotlib.pyplot as plt
import numpy as np

##P0=np.array([0., 0.5])
##P1=np.array([0.2, 1.])
##P2=np.array([1., 0.8])
##
##
##
##fig=plt.figure(1)
##x=[P0[0],P1[0],P2[0]]
##y=[P0[1],P1[1],P2[1]]
##
##plt.plot(x,y,'r-',x,y,'ko',ms=8)
##
##Bezier=lambda t: (1-t)**2*P0+2*t*(1-t)*P1+t**2*P2
##
##xb=[]
##yb=[]
##for t in np.linspace(0.,1.,100):
##    a,b=Bezier(t)
##    xb.append(a)
##    yb.append(b)
##plt.plot(xb,yb,'g-',lw=2)
##
##plt.xticks([])
##plt.yticks([])

fig2=plt.figure(2)

x=np.array([0.,-0.2,1. ])
y=np.array([0.5,1.,0.8])
plt.plot(x,y,'r-',x,y,'ko',ms=8)
t=np.linspace(0.,1.,100)
bx=(1-t)**2*x[0]+2*t*(1-t)*x[1]+t**2*x[2]
by=(1-t)**2*y[0]+2*t*(1-t)*y[1]+t**2*y[2]
plt.plot(bx,by,'g-',lw=2)

plt.xticks([])
plt.yticks([])
plt.axis([x.min()-0.1, x.max()+0.1, y.min()-0.1, y.max()+0.1])
plt.axis('off')
plt.show()
