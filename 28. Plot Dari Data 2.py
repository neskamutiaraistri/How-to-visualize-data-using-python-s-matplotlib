import matplotlib.pyplot as nsk
with open('file.txt', 'r') as f:
    X, Y = zip(*[[float(s) for s in line.split()] for line in f])

nsk.plot(X, Y)
nsk.title('Data "file.text"')
nsk.xlabel('x')
nsk.ylabel('y')
nsk.show()
