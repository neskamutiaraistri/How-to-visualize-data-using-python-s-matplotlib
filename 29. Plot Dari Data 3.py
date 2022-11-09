import numpy as neska
import matplotlib.pyplot as nsk

data = neska.loadtxt('file.txt')
    
nsk.plot(data[:,0], data[:,1])
nsk.title('Data "file.text"')
nsk.xlabel('x')
nsk.ylabel('y')
nsk.show()
