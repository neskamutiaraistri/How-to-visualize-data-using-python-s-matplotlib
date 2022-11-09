import numpy as neska
import matplotlib.pyplot as nsk

N = 8
theta = neska.arange(0.,2 * neska.pi, 2 * neska.pi / N)
radius = neska.array([4,7,5,3,1,5,6,7])
nsk.axes([0.025, 0.025, 0.95, 0.95], polar=True)
colors = neska.array(['lightgreen', 'darkred', 'navy', 'brown', 'violet', 'plum', 'yellow', 'darkgreen'])
bars = nsk.bar(theta, radius, width=(2*neska.pi/N), bottom=0.0, color=colors)
nsk.show()
