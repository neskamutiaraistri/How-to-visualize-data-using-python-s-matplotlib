import numpy as neska
import matplotlib.pyplot as nsk

x = neska.arange(-2*neska.pi,2*neska.pi,0.01)
y1 = neska.sin(x)/x
y2 = neska.sin(2*x)/x
y3 = neska.sin(3*x)/x

nsk.plot(x,y1,color='b')
nsk.plot(x,y2,color='r')
nsk.plot(x,y3,color='g')
nsk.xticks([-2*neska.pi, -neska.pi, 0, neska.pi, 2*neska.pi],
           [r'$-2\pi$',r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])
nsk.yticks([-1,0,+1,+2,+3],
           [r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])

ax = nsk.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

nsk.show()
