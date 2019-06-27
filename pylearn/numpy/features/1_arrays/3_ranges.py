#To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists.

import numpy as np

x = np.arange(10, 30, 5)

print(x)


b = np.arange(12).reshape(4,3)
print(b)

c = np.arange(24).reshape(2,3,4)
print(c)