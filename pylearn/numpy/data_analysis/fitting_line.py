x = [0, 0.5, 1, 1.5, 2.0, 3.0, 4.0, 6.0, 10]
y = [0, -0.157, -0.315, -0.472, -0.629, -0.942, -1.255, -1.884, -3.147]

import numpy as np

p = np.polyfit(x, y, 1)
print(p)
slope, intercept = p
print(slope, intercept)

import matplotlib.pyplot as plt

xfit = np.linspace(0, 10)
yfit = np.polyval(p, xfit)

plt.plot(x, y, 'bo', label='raw data')
plt.plot(xfit, yfit, 'r-', label='fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()