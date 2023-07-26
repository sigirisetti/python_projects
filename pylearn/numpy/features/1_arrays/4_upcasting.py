import numpy as np
from numpy import pi

#
# When operating with arrays of different types,
# the type of the resulting array corresponds to the more general or precise one (a behavior known as upcasting).
#

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print(b.dtype.name)

c = a + b
print(c)
print(c.dtype.name)

d = np.exp(c * 1j)
print(d)
print(d.dtype.name)
