import numpy as np

def func(x, y):
    "return product of x and y"
    return x * y

print(func(2, 3))
print(func(np.array([2, 3]), np.array([3, 4])))