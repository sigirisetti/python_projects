import numpy as np


#
# ndarray.shape, reshape, resize, ravel
#

a = np.floor(10*np.random.random((3,4)))

print(a.shape)
a.ravel()  # returns the array, flattened
a.reshape(6,2)  # returns the array with a modified shape

a.T  # returns the array, transposed
a.T.shape
a.shape

# The reshape function returns its argument with a modified shape, whereas the ndarray.resize method modifies the array itself:
a.resize((2,6))

#If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:
a.reshape(3,-1)

