import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 4)
y = x**3 + 6 * x**2 - 4*x - 24

roots = np.roots([1, 6, -4, -24])
print(roots)

plt.plot(x, y, roots, np.zeros(len(roots)), 'o')
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.show()