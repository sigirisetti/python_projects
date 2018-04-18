import numpy as np
import matplotlib.pyplot as plt

# Area over-estimated with fewer points
x = np.array([0, 0.5, 1, 1.5, 2])
y = x**3

x2 = np.linspace(0, 2)
y2 = x2**3

plt.plot(x, y, label='5 points', color='r')
plt.plot(x2, y2, label='50 points', color='g')
plt.legend()
plt.show()

# using more points will bring back accuracy
x2 = np.linspace(0, 2, 100)
y2 = x2**3

print(np.trapz(y2, x2))
