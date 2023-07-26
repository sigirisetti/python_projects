import numpy as np

a = np.random.random((2, 3))
a

print(a.sum())
print(a.min())
print(a.max())

# By default, these operations apply to the array as though it were a list of numbers, regardless of its shape.
# However, by specifying the axis parameter you can apply an operation along the specified axis of an array:

b = np.arange(12).reshape(3, 4)
print(b)

print(b.sum(axis=0))  # sum of each column
print(b.min(axis=1))  # min of each row
print(b.cumsum(axis=1))  # cumulative sum along each row
