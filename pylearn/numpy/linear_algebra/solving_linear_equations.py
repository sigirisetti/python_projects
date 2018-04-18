import numpy as np
A = np.array([[1, -1, 1],
              [0, 10, 25],
              [20, 10, 0]])

b = np.array([0, 90, 80])

x = np.linalg.solve(A, b)
print(x)
print(np.dot(A,x))

# Let us confirm the solution.
# this shows one element is not equal because of float tolerance
print(np.dot(A,x) == b)

# here we use a tolerance comparison to show the differences is less
# than a defined tolerance.
TOLERANCE = 1e-12
print(np.abs((np.dot(A, x) - b)) <= TOLERANCE)