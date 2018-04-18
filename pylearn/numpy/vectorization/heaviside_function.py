import numpy as np

def heaviside(x):
    x = np.array(x)
    if x.shape != ():
        y = np.zeros(x.shape)
        y[x > 0.0] = 1
        y[x == 0.0] = 0.5
    else: # special case for 0d array (a number)
        if x > 0: y = 1
        elif x == 0: y = 0.5
        else: y = 0
    return y

def f3(x):
    x = np.array(x)
    y1 = (heaviside(x) - heaviside(x - 1)) * x # first interval
    y2 = (heaviside(x - 1) - heaviside(x - 2)) * (2 - x) # second interval
    return y1 + y2

from scipy.integrate import quad
print(quad(f3, -1, 3))