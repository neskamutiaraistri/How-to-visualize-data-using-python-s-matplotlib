import numpy as neska
import matplotlib.pyplot as nsk

data = neska.random.rand(1024, 2)
nsk.scatter(data[:,0], data[:,1])
nsk.show()
