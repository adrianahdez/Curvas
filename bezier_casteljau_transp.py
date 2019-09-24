import matplotlib.pyplot as plt
import numpy as np

#funcion recurvisa
def B(coorArr, i, j, t):
    if j == 0:
        return coorArr[i]
    return B(coorArr, i, j - 1, t) * (1 - t) + B(coorArr, i + 1, j - 1, t) * t

#P=np.array([[0., 0.5],[0.2, 1.],[1., -0.8],[1.2,0.6]])
    
P=np.array([np.array([[2.5, 10.],[4.,12.],[6., 12.]]),
            np.array([[6., 12.],[8.,12.],[9., 10.]]),
             np.array([[9., 10.],[10.,8.],[10., 6.]] ),
             np.array([[10., 6.],[8.,7.],[6., 7.]] ),
             np.array([[6., 7.],[4.,7.],[2., 6.]] ),
             np.array([[2., 6.],[0.8,5.],[0.8, 4.]] ),
             np.array([[0.8, 4.],[0.8,3.],[1.7, 1.7],[2., 1.]] )
            ])
    
#P=np.array([np.array([[2.5, 10.],[4.,12.],[6., 12.]]), 
#            np.array([[6., 12.],[8.,12.],[9., 10.]]),
 #           np.array([[9., 10.],[10.,8.],[10., 6.]] ), 
  #          np.array([[10., 6.],[8.,7.],[6., 7.]] ),
   #         np.array([[6., 7.],[4.,7.],[2., 6.]] ), 
    #        np.array([[2., 6.],[0.8,5.],[0.8, 4.]] ),
     #       np.array([[0.8, 4.],[0.8,3.],[1.7, 1.7],[2., 1.]] ),
      #      np.array([[2., 1.],[3., 0.5],[5., 0.8],[6., 1.]] ),
       #     np.array([[6., 1.],[7., 1.4],[9., 2.],[10., 3.]] ),
        #    np.array([[10., 6.],[10., 3.]] ),
         #   np.array([[10., 3.],[10., 1.],[13.5, 1.] ] ) ])

#P=np.array(([[2.5, 10.],[6., 12.],[9., 10.],[10.,8.]])\
          # ,np.array([[2.5, 10.],[6., 12.],[9., 10.],[10.,8.]])\
          # ,np.array([[2.5, 10.],[6., 12.],[9., 10.],[10.,8.]]))

##n=4
print(P)
xr=P[:,0]

yr=P[:,1]

fig=plt.figure(1)

##plt.text(-0.06, 0.5, 'P0')
##plt.text(0.15, 1.01, 'P1')
##plt.text(1.05, 0.8, 'P2')
##plt.text(1.15, 0.57, 'P3')


xb=[]
yb=[]

for pt in P:
    x= pt[:,0]
    y=pt[:,1]
    m=x.size
    for t in np.linspace(0.,1.,25):
        a = B(x, 0, m - 1, t)
        b = B(y, 0, m - 1, t)
        xb.append(a)
        yb.append(b)
    plt.plot(xb,yb,'go', ms=4)

    plt.plot(x,y,'r-',x,y,'ko',ms=8)

#plt.xticks([])
#plt.yticks([])
#plt.axis('off')

plt.axis([min(xr)-0.065,max(xr)+.05,min(yr)-0.05,max(yr)+0.05])
#plt.axis([0,15,0,15])

#plt.axis([-0.5,5,-0.5,5])
#plt.axis([0,15,0,15])

plt.show()