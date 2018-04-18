import numpy as np
from sympy import Matrix

A = np.array([[3, 2, 1],
              [2, 1, 1],
              [6, 2, 4]])

print(np.linalg.det(A))
print(np.linalg.inv(A))

b = np.array([3, 0, 6])

print(np.linalg.solve(A, b))