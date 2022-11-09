from mpl_toolkits.mplot3d import Axes3D
import numpy as neska
import matplotlib.pyplot as nsk

fig = nsk.figure()
ax = Axes3D(fig)
X = neska.arange(-2,2,0.1)
Y = neska.arange(-2,2,0.1)
X,Y = neska.meshgrid(X,Y)
def f(x,y):
    return (1 - y**5 + x**5)*neska.exp(-x**2-y**2)
ax.plot_surface(X,Y,f(X,Y), rstride=1, cstride=1)
nsk.show()
