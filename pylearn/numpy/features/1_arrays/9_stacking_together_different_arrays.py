import numpy as np
from numpy import newaxis

a = np.floor(10*np.random.random((2,2)))
print(a)

b = np.floor(10*np.random.random((2,2)))
print(b)

print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(np.column_stack((a,b)))     # returns a 2D array

print()
print()

a = np.array([4.,2.])
b = np.array([3.,8.])

print(np.column_stack((a,b)))     # returns a 2D array
print(np.hstack((a,b)))           # the result is different
print(a[:,newaxis])               # this allows to have a 2D columns vector
print(np.column_stack((a[:,newaxis],b[:,newaxis])))
print(np.hstack((a[:,newaxis],b[:,newaxis])))   # the result is the same