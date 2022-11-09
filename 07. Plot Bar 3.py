import numpy as neska
import matplotlib.pyplot as nsk

index = neska.arange(5)
values = [5,7,3,4,6]
std = [0.8,1,0.4,0.9,1.3]

nsk.title('Diagram Batang')
nsk.bar(index,values,yerr=std,error_kw={'ecolor':'0.1','capsize':6},alpha=0.7,label='first')
nsk.xticks(index+0.4, ['A','B','C','D','E'])

nsk.legend(loc=2)
nsk.show()
