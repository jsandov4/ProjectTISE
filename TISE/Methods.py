import numpy as np
import math
from numpy import *
import matplotlib.pyplot as plt 

def D2_LegPolyn(itype,N):
    x0 =-1.0
    xf = 1.0
    dx = (xf-x0)/(N-1.0)
    # 2 additional points to avoid lost of them in deriv
    x = np.linspace(x0,xf,N)
    xaux = np.linspace(x0-2*dx,xf+2*dx,N+4)
    yaux = LegPolyn(itype,xaux)
    x2,dy = secondDer(xaux,yaux,dx)
    return x,dy
def LegPolyn(itype,x):
    nsize = len(x)
    if(itype == 0):
        y = np.array([1.0 for i in range(nsize)],float)
    if(itype == 1):
        y = x
    if(itype == 2):
        y = 0.5*(3*(x**2)-1.0)
    if(itype == 3):
        y = 0.5*(5.0*(x**3)-3.0*x)
    if(itype == 4):
        y = (35.0*(x**4)-30.0*(x**2)+3.0)/8.0
    if(itype == 5):
        y = (63.0*(x**5)-70.0*(x**3)+15.0*x)/8.0
    if(itype == 6):
        y = (231.0*(x**6)-315.0*(x**4)+105.0*(x**2)-5.0 )/16.0
    if(itype == 7):
        y = (429.0*(x**7)-693.0*(x**5)+315.0*(x**3)-35.0*x)/16.0
    if(itype == 8):
        y = (6435.0*(x**8)-12012.0*(x**6)+6930.0*(x**4)-1260.0*(x**2)+35.0)/128.0
    if(itype == 9):
        y = (12155.0*(x**9)-25740.0*(x**7)+18018.0*(x**5)-4620.0*(x**3)+315.0*x)/128.0
    if(itype == 10):
        y = (46189.0*(x**10)-109395.0*(x**8)+90090.0*(x**6)-30030.0*(x**4)+3465.0*(x**2)-63.0)/256
    return y
        
def derivative(x,y,dx):
    nsize = len(y)
    dy = np.array([0.0 for i in range(nsize-2)],float)
    x2 = np.array([0.0 for i in range(nsize-2)],float)
    for k in range(1,nsize-1):
        y1 = y[k-1]
        y3 = y[k+1]
        dy[k-1] = (y3 - y1)/(2*dx)
        x2[k-1] = x[k]
    return x2,dy


def secondDer(x,y,dx):
    x2,dy = derivative(x,y,dx)
    x3,ddy = derivative(x2,dy,dx)
    return x3,ddy

def integrate(x,y,dx):
    suma = 0.0
    nsize = len(x)
    for k in range(nsize-1):
        f1 = y[k]
        f2 = y[k+1]
        suma = suma + (f1+f2)*dx/2.0
    return suma

def normalize(vector):
    suma = 0.0
    vector2 = np.array([0.0 for i in range(len(vector))],float)
    for i in range(len(vector)):
        suma = suma + vector[i]**2
    if (suma <= 0.0001):
        suma = 1.0
    suma = sqrt(suma)
    for j in range(len(vector)):
        vector2[j]=vector[j]/suma
    return vector2

def buildMatrix(N,nbase):
    x0 =-1.0
    xf = 1.0
    dx = (xf-x0)/(N-1.0)
    x = np.linspace(x0,xf,N)
    matrix = np.zeros((nbase,nbase))
    y1 = np.array([0]*N)
    y2 = np.array([0]*N)
    val = np.array([0]*N)
    for i in range(nbase):
        for j in range(nbase):
            y1 = LegPolyn(i,x)
            x2,y2 = D2_LegPolyn(j,N)
            for k in range(N):
                val[k] = y1[k]*y2[k]
            val2 = normalize(val)
            matrix[i][j] = integrate(x,val2,dx)
            #matrix[j][i] = matrix[i][j]
    return matrix



if __name__ == __main__:

    x0 = -1.0
    xf = 1.0

    N = 1000
    nbases = 4


    dx = (xf-x0)/(N-1)
    x = np.linspace(x0,xf,N)

    i = 4
    j  = 6
    f1 = LegPolyn(i,x)
    f2 = LegPolyn(j,x)
    f12 = f1*f2
    print(i,j,integrate(x,f12,dx))

    m =  buildMatrix(N,nbases)

    print(m)

    plt.plot(x,f1)
    plt.plot(x,f2)
    #plt.show()


    A = np.mat("3 2; 2 0")

    #print "A : \n",A
    w,v = np.linalg.eig(m)

    #print w[0]
    #print v
    #print w
