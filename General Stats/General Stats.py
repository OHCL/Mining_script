import numpy as np
import matplotlib.pyplot as plt

matrix = np.loadtxt('GeologicalModel.csv',skiprows=1,usecols=(0,1,2),delimiter=',',dtype=np.float)
#print(matrix)

#print(len(matrix[:,0]))

xmin, xmax = np.min(matrix[:,0]), np.max(matrix[:,0])
xlen = xmax - xmin

print('Minimo: ' + str(xmin) + '. Maximo: ' + str(xmax) + '. Largo total: ' + str(xlen))

xset = []
for x in set (matrix[:,0]):
    xset.append(x)

yset = []
for y in set (matrix[:,1]):
    xset.append(x)
#print (xset)
xsize = xset[1] - xset[0]
xnodes = xlen / xsize
#print(xnodes)

value = matrix[:,0]
print ('N datos: ' + str(len(value)))
print ('Promedio: ' + str(np.mean(value)))
print ('Varianza: ' + str(np.var(value)))
print ('STD: ' + str(np.sqrt(np.var(value))))
print ('MIN: ' + str(xmin))
print ('MAX: ' + str(xmax))