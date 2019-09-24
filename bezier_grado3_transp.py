import matplotlib.pyplot as plt
import numpy as np

P=np.array([[0., 0.5],[0.2, 1.],[1., 0.8],[1.2,0.6]])  
x=P[:,0]
y=P[:,1]

##fig=plt.figure(1)
##
####plt.text(-0.06, 0.5, 'P0')
####plt.text(0.15, 1.01, 'P1')
####plt.text(1.05, 0.8, 'P2')
####plt.text(1.15, 0.57, 'P3')
##
##
##
##def Bezier(t):
##    qx=[]
##    qy=[]
##    rx=[]
##    ry=[]
##    Q=[]
##
##    for k in range(0,3):
##        q=(1-t)*P[k]+t*P[k+1]
##        Q.append(q)
##        qx.append(q[0])
##        qy.append(q[1])
##    for k in range(0,2):
##        R=(1-t)*Q[k]+t*Q[k+1]
##        rx.append(R[0])
##        ry.append(R[1])
##        
##    B=(1-t)**3*P[0]+3*t*(1-t)**2*P[1]+3.*t**2*(1-t)*P[2]+t**3*P[3]
##
##    plt.plot(qx,qy,'b:')
##    plt.plot(qx,qy,'rx')
##    plt.plot(rx,ry,'g-')
##    plt.plot(rx,ry,'co')
##    return B
##
##
##
##
##xb=[]
##yb=[]
##for t in np.linspace(0.,1.,25):
##    a,b=Bezier(t)
##    xb.append(a)
##    yb.append(b)
##plt.plot(xb,yb,'go')
##
##plt.plot(x,y,'r-')
##plt.plot(x,y,'ko',ms=8)
##
##plt.xticks([])
##plt.yticks([])
##
##plt.axis([min(x)-0.065,max(x)+.05,min(y)-0.05,max(y)+0.05])

fig=plt.figure(2)
t=np.linspace(0.,1.,105)

Bx=(1-t)**3*x[0]+3*t*(1-t)**2*x[1]+3.*t**2*(1-t)*x[2]+t**3*x[3]
By=(1-t)**3*y[0]+3*t*(1-t)**2*y[1]+3.*t**2*(1-t)*y[2]+t**3*y[3]

plt.plot(Bx,By,'g-',lw=2)

plt.plot(x,y,'r-',x,y,'ko',ms=8)

plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.axis([min(x)-0.065,max(x)+.05,min(y)-0.05,max(y)+0.05])
plt.show()