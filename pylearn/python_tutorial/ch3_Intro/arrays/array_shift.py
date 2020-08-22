import numpy as np
from scipy.ndimage.interpolation import shift

arr1 = [1, 2, 3, 4 ,5]
arr2 = [float('nan'), 2, 3, 4 ,5]
print(np.array(arr1) != np.array(arr2))

np_arr1 = np.array(arr1)
np_arr2 = shift(np_arr1, -1, cval=np_arr1[-1])
print(np_arr1)
print(np_arr2)
print(np_arr1 != np_arr2)