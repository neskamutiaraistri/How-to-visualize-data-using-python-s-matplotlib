import numpy as neska
import matplotlib.pyplot as nsk

index = neska.arange(5)
values1 = [5,7,3,4,6]
values2 = [6,5,4,5,5]
values3 = [4,6,5,4,6]
bw = 0.3

nsk.axis([0,5,0,8])
nsk.title('Diagram Batang Multiserial',fontsize=20)
nsk.barh(index,values1,bw,color='b')
nsk.barh(index+bw,values2,bw,color='g')
nsk.barh(index+2*bw,values3,bw,color='r')
nsk.yticks(index+1.5*bw, ['A','B','C','D','E'])

nsk.show()
