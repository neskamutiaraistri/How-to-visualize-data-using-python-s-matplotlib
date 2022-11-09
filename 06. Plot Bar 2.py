import numpy as neska
import matplotlib.pyplot as nsk

index = neska.arange(5)
values = [5,7,3,4,6]

nsk.bar(index,values)
nsk.xticks(index+0.4, ['A','B','C','D','E'])
nsk.show()
