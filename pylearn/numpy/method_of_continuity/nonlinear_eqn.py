import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def dxdL(x, Lambda):
    return -x**2 / (-5.0 + 2 * Lambda * x)

x0 = 6.0/5.0
Lspan = np.linspace(0, 1)
x = odeint(dxdL, x0, Lspan)

plt.plot(Lspan, x)
plt.xlabel('$\lambda$')
plt.ylabel('x')
plt.show()