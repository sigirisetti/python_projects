from scipy.special import jn, jn_zeros
import matplotlib.pyplot as plt
import numpy as np

Bi = 1

def f(x):
    return x * jn(1, x) - Bi * jn(0, x)

X = np.linspace(0, 30, 200)
plt.plot(X, f(X))
plt.show()