import numpy as np

a = np.floor(10*np.random.random((2,12)))

print(a)
print(np.hsplit(a,3))   # Split a into 3
print(np.hsplit(a,(3,4)))   # Split a after the third and the fourth column
