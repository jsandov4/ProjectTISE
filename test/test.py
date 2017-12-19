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
	for i in range(nt-2):
		val = abs( dy[i]-cos(xx[i]) )
		assert ( val <= 0.01) , "Bad derivative"

def test_derivative2():
	nt = 1000
	dx = 2*pi/nt
	x = np.linspace(0,2*pi,nt)
	y = sin(x)
	yp = 0.0
	xx,dy = Methods.derivative2(x,y,dx)
	for i in range(nt-4):
		val = abs( dy[i]+sin(xx[i]) )
		assert ( val <= 0.01) , "Bad second derivative"

def test_integrate():
	nt = 1000
	dx = (pi/2)/nt
	x = np.linspace(0,pi/2,nt)
	y = cos(x)
	val1 = Methods.integrate(y,dx)

	dx = 1/nt
	x = np.linspace(0,1,nt)
	y = x**3
	val2 = Methods.integrate(y,dx)

	dx = 2/nt
	x = np.linspace(-1,1,nt)
	y = 0.5*(5.0*(x**3)-3.0*x) # exact P3 (third legendre poly)
	val3 = Methods.integrate(y*y,dx)

	assert ( abs(val1 - sin(pi/2.0) ) <= 0.01) , "Bad first integration"
	assert ( abs(val2 - 0.25)     <= 0.01) , "Bad second integration"
	assert ( abs(val3 - 0.2857)   <= 0.01) , "Bad third integration"

def test_normalize():
	nt = 1000
	dx = 2.0/(nt-1.0)
	x = np.linspace(-1,1,nt)
	y2 = np.zeros((nt))
	for i in range(5):
		y = Methods.normalize( Methods.recursiveLP(i,x),dx )
		y2 = y*y
		val = Methods.integrate(y2,dx)
		assert ( abs(val - 1.0) <= 0.01 ), 'bad Normalize'

def test_LegendrePolynomials():
	nt = 100
	dx = 2.0/nt
	y2 = np.zeros(nt)
	x = np.linspace(-1,1,nt)
	y = Methods.recursiveLP(3,x)
	y2 = 0.5*(5.0*(x**3)-3.0*x) # exact P3 (third legendre poly)
	for i in range(nt):
		val = abs(y[i]-y2[i])
		assert ( val <= 0.1) , "Bad LP"
