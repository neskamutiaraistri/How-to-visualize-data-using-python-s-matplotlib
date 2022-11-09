import math
import numpy as neska
import matplotlib.pyplot as nsk

t = neska.arange(0,5,0.01)
y1 = neska.sin(math.pi*t)
y2 = neska.sin(math.pi*t+math.pi/2)
y3 = neska.sin(math.pi*t-math.pi/2)

nsk.plot(t,y1,'b--',t,y2,'g',t,y3,'r-.')
nsk.show()
