import numpy as np
from scipy.integrate import simps, romb

a = 0.0; b = np.pi / 4.0;
N = 10  # this is the number of intervals

x = np.linspace(a, b, N)
y = np.cos(x)

t = np.trapz(y, x)
s = simps(y, x)
a = np.sin(b) - np.sin(a)

print('trapz = {0} ({1:%} error)'.format(t, (t - a)/a))
print('simps = {0} ({1:%} error)'.format(s, (s - a)/a))
print('analy = {0}'.format(a))