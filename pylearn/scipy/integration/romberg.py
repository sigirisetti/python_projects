import numpy as np

from scipy.integrate import quad, romberg

a = 0.0
b = np.pi / 4.0

print(quad(np.sin, a, b))
print(romberg(np.sin, a, b))