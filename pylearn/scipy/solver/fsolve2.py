from scipy.optimize import fsolve
import numpy as np


def f(x):
    return np.cos(x)


# the comma after sol makes it return a float
sol, = fsolve(f, x0=1.5)

print(sol)
print(np.pi / 2)

