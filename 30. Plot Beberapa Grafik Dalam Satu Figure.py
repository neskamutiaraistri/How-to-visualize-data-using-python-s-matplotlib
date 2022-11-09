import math
import numpy as neska
import matplotlib.pyplot as nsk

t = neska.arange(0,5,0.1)
y1 = neska.sin(math.pi*t)
y2 = neska.sin(math.pi*t+math.pi/2)
y3 = neska.sin(math.pi*t-math.pi/2)

nsk.subplot(3,1,1)
nsk.title('Fungsi y1')
nsk.plot(t,y1,'b--')

nsk.subplot(3,1,2)
nsk.title('Fungsi y2')
nsk.plot(t,y2,'g')

nsk.subplot(3,1,3)
nsk.title('Fungsi y3')
nsk.plot(t,y3,'r-.')

nsk.show()
