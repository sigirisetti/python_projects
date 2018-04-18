import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30, 40])

print(a * b[:, np.newaxis])