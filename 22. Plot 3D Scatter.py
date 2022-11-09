from mpl_toolkits.mplot3d import Axes3D
import numpy as neska
import matplotlib.pyplot as nsk

xs = neska.random.randint(30,40,100)
ys = neska.random.randint(20,30,100)
zs = neska.random.randint(10,20,100)
xs2 = neska.random.randint(50,60,100)
ys2 = neska.random.randint(30,40,100)
zs2 = neska.random.randint(50,70,100)
xs3 = neska.random.randint(10,30,100)
ys3 = neska.random.randint(40,50,100)
zs3 = neska.random.randint(40,50,100)

fig = nsk.figure()
ax = Axes3D(fig)
ax.scatter(xs,ys,zs)
ax.scatter(xs2,ys2,zs2,c='r',marker='^')
ax.scatter(xs3,ys3,zs3,c='g',marker='*')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
nsk.show()
