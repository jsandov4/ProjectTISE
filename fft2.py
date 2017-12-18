
import numpy as np
import math
from numpy import *
from threading import *
from numpy.fft import fft
from numpy.fft import ifft
import matplotlib.pyplot as plt 

print pi
N = 1024
x = linspace(0,2*pi,N)
ik = 1j*hstack((range(0,N/2+1), range(-N/2+1,0))); # i * wave number vector (matla
ik2 = ik#*ik; # multiplication factor for second derivative
u = cos(x)
u2d = 3*x*x
u_hat = fft(u)
v_hat = ik2 * u_hat
v = real(ifft(v_hat)) # imaginary part should be at machine precision level


plt.plot(x,u)
plt.show()
plt.clf()
plt.plot(x,u2d)
plt.show()
plt.clf()
plt.plot(x,v)
plt.show()