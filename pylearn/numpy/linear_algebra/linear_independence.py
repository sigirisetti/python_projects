import numpy as np

v1 = [6, 0, 3, 1, 4, 2];
v2 = [0, -1, 2, 7, 0, 5];
v3 = [12, 3, 0, -19, 8, -11];

A = np.row_stack([v1, v2, v3])

# matlab definition
eps = np.finfo(np.linalg.norm(A).dtype).eps
print(np.finfo(np.linalg.norm(A).dtype))

TOLERANCE = max(eps * np.array(A.shape))

U, s, V = np.linalg.svd(A)
print(s)
print(np.sum(s > TOLERANCE))

TOLERANCE = 1e-14
print(np.sum(s > TOLERANCE))