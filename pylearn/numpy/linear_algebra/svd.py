import numpy as np
A = np.array([[1, -1, 1],
              [0, 10, 25],
              [20, 10, 0]])

b = np.array([0, 90, 80])

# determine number of independent rows in A we get the singular values
# and count the number greater than 0.
TOLERANCE = 1e-12
u, s, v = np.linalg.svd(A)
print('Singular values: {0}'.format(s))
print('# of independent rows: {0}'.format(np.sum(np.abs(s) > TOLERANCE)))

# to illustrate a case where there are only 2 independent rows
# consider this case where row3 = 2*row2.
A = np.array([[1, -1, 1],
              [0, 10, 25],
              [0, 20, 50]])

u, s, v = np.linalg.svd(A)

print('Singular values: {0}'.format(s))
print('# of independent rows: {0}'.format(np.sum(np.abs(s) > TOLERANCE)))