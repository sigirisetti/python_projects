import numpy as np

# Without numpy
w = [0.1, 0.25, 0.12, 0.45, 0.98];
x = [9, 7, 11, 12, 8];
y = 0
for wi, xi in zip(w,x):
   y += wi * xi**2
print(y)

# With numpy

import numpy as np
w = np.array([0.1, 0.25, 0.12, 0.45, 0.98])
x = np.array([9, 7, 11, 12, 8])
y = np.sum(w * x**2)
print(y)

# Quadratic form
import numpy as np
w = np.array([0.1, 0.25, 0.12, 0.45, 0.98])
x = np.array([9, 7, 11, 12, 8])
y = np.dot(x, np.dot(np.diag(w), x))
print(y)


import numpy as np

w = np.array([0.1, 0.25, 0.12, 0.45, 0.98])
x = np.array([9, 7, 11, 12, 8])
y = np.array([2, 5, 3, 8, 0])

print(np.sum(w * x * y))
print(np.dot(w, np.dot(np.diag(x), y)))