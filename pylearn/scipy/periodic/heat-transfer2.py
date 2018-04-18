from pycse import *  # contains the ode integrator with events

from scipy.special import jn, jn_zeros
import matplotlib.pyplot as plt
import numpy as np

Bi = 1

def f(x):
    "function we want roots for"
    return x * jn(1, x) - Bi * jn(0, x)

def fprime(f, x):
    "df/dx"
    return x * jn(0, x) - Bi * (-jn(1, x))

def e1(f, x):
    "event function to find zeros of f"
    isterminal = False
    value = f
    direction = 0
    return value, isterminal, direction

f0 = f(0)
xspan = np.linspace(0, 30, 200)

x, fsol, XE, FE, IE = odelay(fprime, f0, xspan, events=[e1])

plt.plot(x, fsol, '.-', label='Numerical solution')
plt.plot(xspan, f(xspan), '--', label='Analytical function')
plt.plot(XE, FE, 'ro', label='roots')
plt.legend(loc='best')
plt.show()

for i, root in enumerate(XE):
    print('root {0} is at {1}'.format(i, root))