import io
import numpy as np
import math
from numpy import *
from TISE import Methods

def test_derivative():
	nt = 1000
	dx = 2*pi/nt
	x = np.linspace(0,2*pi,nt)
	y = sin(x)
	yp = 0.0
	xx,dy = Methods.derivative(x,y,dx)
	x1 = xx[10]
	y1 = dy[10]
	(x1,y1,cos(x1))
	assert (abs(y1 - cos(x1) <= 0.01)) , "Bad derivative"

def test_secondDerivative():
	nt = 100
	dx = 2*pi/nt
	x = np.linspace(0,2*pi,nt)
	y = sin(x)
	yp = 0.0
	xx,dy = Methods.secondDer(x,y,dx)

	x1 = xx[10]
	y1 = dy[10]	
	assert (abs(y1 - (-sin(x1)) <= 0.01)) , "Bad second derivative"

def test_integrate():
	nt = 100
	dx = (pi/2)/nt
	x = np.linspace(0,pi/2,nt)
	y = cos(x)
	val = Methods.integrate(x,y,dx)
	assert (abs(val - 1 <= 0.01)) , "Bad second integration"

def test_normalize():
	nt = 100
	dx = 2*pi/nt
	x = np.linspace(0,2*pi,nt)
	y = cos(x)
	yn = Methods.normalize(y)
	val = Methods.integrate(x,yn,dx)
	assert (abs(val - 1 <= 0.01)) , "Bad normalization"