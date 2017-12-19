import numpy as np
import math
from numpy import *
import matplotlib.pyplot as plt 
        
def derivative(x,y,dx):
    nsize = len(x)
    dy = np.array([0.0 for i in range(nsize-2)],float)
    x2 = np.array([0.0 for i in range(nsize-2)],float)
    for k in range(1,nsize-1):
        y1 = y[k-1]
        y3 = y[k+1]
        dy[k-1] = (y3 - y1)/(2*dx)
        x2[k-1] = x[k]
    return x2,dy

def derivative2(x,y,dx):
    x2,dy = derivative(x,y,dx)
    x3,ddy = derivative(x2,dy,dx)
    return x3,ddy

def integrate(y,dx):
    suma = 0.0
    nsize = len(y)
    for k in range(nsize-1):
        f1 = y[k]
        f2 = y[k+1]
        suma = suma + (f1+f2)*dx/2.0
    return suma

def normalize(array,dx):
    array2 = np.zeros(len(array))
    for i in range(len(array)):
        array2[i] = array[i]*array[i]*dx
    suma = 0.0
    for i in range(len(array)):
        suma = suma + array2[i]
 
    for i in range(len(array)):
        val = array[i]/sqrt(suma)
        if( math.isnan(val) ):
            val = 0.0
        array2[i] = val
    return array2

def combina(n,p):
    num = math.factorial(n)
    den = math.factorial(p)*math.factorial(n-p)
    return num/den

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

def Hij(i,j,N,itype):
    if(itype == 0):
        x0 =-1.0
        xf = 1.0
        dx = (xf-x0)/(N-1.0)  
        x = np.linspace(x0,xf,N)
        yi = normalize(recursiveLP(i,x),dx)
        xl = np.linspace(x0-2*dx,xf+2*dx,N+4)
        yj = normalize(recursiveLP(j,xl),dx)
       
    else:
        x0 = 0.0
        xf = 2.0*pi
        dx = (xf-x0)/N 
        x = np.linspace(x0,xf,N)
        yi = normalize(fourierBasis(i,x),dx)
        xl = np.linspace(x0-2*dx,xf+2*dx,N+4)
        yj = normalize(fourierBasis(j,xl),dx)
       

    x2,ddyj = derivative2(xl,yj,dx)
    #ddyjn = normalize(ddyj,dx)
    integ = -integrate(yi*ddyj,dx)

    return integ


def buildMatrix(N,nbase,itype,v0):

    matrix = np.zeros((nbase,nbase))

    for i in range(nbase):
        for j in range(nbase):
            if(i == j):
                v0val = v0
            else:
                v0val = 0.0        
            matrix[i][j] = Hij(i,j,N,itype) + v0val
            
    return matrix



def main(): # pragma: no cover
    import os
    import sys

    filename = sys.argv[1]
    # Reading the input
    f = open(filename,'r')
    allLines = f.readlines()
    itipo = int(allLines[1])
    nbase = int(allLines[3])
    N = int(allLines[5])
    v0 = float(allLines[7])


    #N = 1000 # number of points,x 
    #nbase = 10 # size of basis set
    #itipo = 0 # 0 : LegPoly, 1: Fourier
    #v0 = 0.0 # input potential constant

    if (itipo == 0):
        dx = 2.0/(N-1.0)
        x = np.linspace(-1,1,N) 
    else:
        dx = 2.0*pi/N
        x = np.linspace(0,2.0*pi,N) 

    m = buildMatrix(N,nbase,itipo,v0)
    oldVal, oldEvect = np.linalg.eig(m)
    newVal = np.zeros(nbase)
    newEvect = np.zeros((nbase,nbase))

# draw stuff
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)



# Organize the eigenvect and eigenval
# according to energy
    minval = 10000
    for k in range(nbase):
        for i in range(nbase):
            if(oldVal[i].real < minval):
                minval = oldVal[i].real
                imin = i
        newVal[k] = oldVal[imin].real
        oldVal[imin] = abs(1000*10)
        for j in range(nbase):
            newEvect[j,k] = oldEvect[j,imin].real
        minval = oldVal[imin].real

# construct the superposition
    for k in range(nbase):
        y = np.zeros(N)
        yaux = np.zeros(N)
        for j in range(nbase):
            cki = newEvect[j,k]
            yaux = cki*normalize(recursiveLP(j,x),dx)
            y = y + yaux
        
        ax1.plot(x,y, label="|"+str(k)+">")
        ax2.plot([1,2],[newVal[k],newVal[k]], label="E"+str(k) )
    ax1.legend()
    ax2.legend()
    plt.legend()   
    plt.show()
    
if __name__ == "__main__":
    main()