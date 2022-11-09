import numpy as neska
import matplotlib.pyplot as nsk

x0 = neska.arange(8)
y1 = neska.array([4,3,2,1,2,4,6,6])
y2 = neska.array([5,4,2,1,3,4,5,6])

nsk.ylim(-7,7)
nsk.bar(x0,y1,0.9,facecolor='r')
nsk.bar(x0,-y2,0.9,facecolor='g')
nsk.xticks(())
for x, y in zip(x0,y1):
    nsk.text(x + 0.4, y + 0.05, '%d' % y, ha='center', va='bottom')
for x, y in zip(x0, y2):
    nsk.text(x + 0.4, -y - 0.05, '%d' % y, ha='center', va='top')
nsk.show()
