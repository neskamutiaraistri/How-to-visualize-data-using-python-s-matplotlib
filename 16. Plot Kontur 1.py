import numpy as neska
import matplotlib.pyplot as nsk

dx = 0.01; dy = 0.01
x = neska.arange(-2.5,2.5,dx)
y = neska.arange(-2.5,2.5,dy)
X,Y = neska.meshgrid(x,y)

def f(x,y):
    return (1 - y**5 + x**5)*neska.exp(-x**2-y**2)
C = nsk.contour(X,Y,f(X,Y),8,colors='black')
nsk.contourf(X,Y,f(X,Y),8)
nsk.clabel(C, inline=1, fontsize=10)
nsk.show()
