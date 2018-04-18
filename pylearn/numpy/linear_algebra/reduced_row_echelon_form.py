import numpy as np
from sympy import Matrix

A = np.array([[3, 2, 1],
              [2, 1, 1],
              [6, 2, 4]])

rA, pivots =  Matrix(A).rref()
print(rA)