import numpy as neska
import matplotlib.pyplot as nsk

x = neska.arange(-2*neska.pi,2*neska.pi,0.01)
y = neska.sin(3*x)/x

nsk.plot(x,y)
nsk.show()
