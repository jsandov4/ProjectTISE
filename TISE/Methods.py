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
    yaux = recursiveLP(itype,xaux)
    x2,dy = secondDer(xaux,yaux,dx)
    return x,dy

        
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

def recursiveLP(n,x):
    size = len(x)
    y = np.zeros((size))
    for ix in range(size):
        for k in range(n+1):
            tt = ((x[ix]-1.0)/2.0)**k
            y[ix] = y[ix]+combina(n,k)*combina(n+k,k)*tt
            
    return y

def fourierBasis(n,x):
    size = len(x)
    length = 2.0 # domain from -1 to 1
    y = np.zeros((size))
    for ix in range(size):
        tt = math.pi*n/length 
        y[ix] = cos(x[ix]*tt)+sin(x[ix]*tt)
    return y

def combina(n,p):
    num = math.factorial(n)
    den = math.factorial(p)*math.factorial(n-p)
    return num/den


def main(): # pragma: no cover
    x0 =-1.0
    xf = 1.0
    N = 100
    nbases = 4
    nt = 1000
    dx = 2.0/nt
    x = np.linspace(-1,1,nt)
    for i in range(5):
        y = fourierBasis(i,x)
        plt.plot(x,y)
    #  yaux = recursiveLP(4,x)
    #  x2,dy = secondDer(x,yaux,dx)
    #plt.plot(x2,dy)
    #plt.plot(x,yaux)
    plt.show()


if __name__ == '__main__':
    main()