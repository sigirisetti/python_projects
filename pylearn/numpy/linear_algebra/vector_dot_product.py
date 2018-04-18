import numpy as np

a = np.array([0, 1, 2])
print(a.shape)
print(a)
print(a.T)


print(np.dot(a, a))
print(np.dot(a, a.T))
print(a @ a)
print(np.sum(a @ a))


b = np.array([[0, 1, 2]])
print(b.shape)
print(b)
print(b.T)

# print(np.dot(b, b))    # this is not ok, the dimensions are wrong.
# print(np.dot(b, b.T))
# print(np.dot(b, b.T).shape)
