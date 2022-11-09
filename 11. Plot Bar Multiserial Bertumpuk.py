import numpy as neska
import matplotlib.pyplot as nsk

index = neska.arange(4)
series1 = neska.array([3,4,5,3])
series2 = neska.array([1,2,2,5])
series3 = neska.array([2,3,3,4])

nsk.axis([0,15,-0.5,3.5])
nsk.title('Diagram Batang Bertumpuk Multiserial')
nsk.barh(index,series1,color='r')
nsk.barh(index,series2,color='b',left=series1)
nsk.barh(index,series3,color='g',left=(series2+series1))
nsk.yticks(index+0.4, ['Sep21','Okt21','Nov21','Des21'])

nsk.show()
