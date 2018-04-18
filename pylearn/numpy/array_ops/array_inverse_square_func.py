import numpy as np

def f(x):
    "return the inverse square of x"
    x = np.array(x)
    return 1.0 / x**2

print(f(3))
print(f([4,5]))