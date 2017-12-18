import numpy as np
import math
from numpy import *
from threading import *
from numpy.fft import fft
from numpy.fft import ifft
import matplotlib.pyplot as plt 

pii=math.pi
x0 =-1
xf = 1
nt = 64
xsize = xf-x0
p = [0]*nt
x = np.linspace(x0,xf,nt)
y = exp(cos(x))#x**2#sin(x) + cos(2*x)
Fy = fft(y)

for k in range(nt):
    i = k + 1
    if (i <= (nt/2 + 1 ) ):
        nx = i - 1
    else:
        nx = i - 1 - nt
    #print i,nx
    if (nx == 0):
        xp = 0
    else:
        xp = 2*pii*nx/xsize

    p[k] = -xp**2

Fyp = Fy*p
#plt.plot(p)
dx2 = ifft(Fyp)

plt.plot(x,real(dx2))
plt.show()