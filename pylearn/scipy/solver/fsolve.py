from scipy.optimize import fsolve
import numpy as np

sol, = fsolve(lambda x: 2.5 - np.sqrt(x), 8)
print(sol)


def f(x):
    return np.cos(x)

sol, = fsolve(f, x0=1.5) # the comma after sol makes it return a float
print(sol)
print(np.pi / 2)