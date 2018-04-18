from scipy.integrate import quad

print(quad(lambda x:x**3, 0 ,2))

x2 = lambda x: x**2
print(quad(x2, 0, 4))

import numpy as np

invexp = lambda x: np.exp(-x)
print(quad(invexp, 0, np.inf))

from scipy.integrate import quad

ans, err = quad(lambda x: x**3, 0, 2)
print(ans)

from scipy.integrate import quad

def integrand(x):
    return x**3

ans, err = quad(integrand, 0, 2)
print(ans)