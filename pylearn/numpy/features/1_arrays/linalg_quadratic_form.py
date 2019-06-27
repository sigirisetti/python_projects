import numpy as np
w = np.array([0.1, 0.25, 0.12, 0.45, 0.98])
x = np.array([9, 7, 11, 12, 8])
print(np.diag(w))
y = np.dot(x, np.dot(np.diag(w), x))
print(y)