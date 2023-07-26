# linspace that receives as an argument the number of elements that we want, instead of the step

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * pi, 100)

print(x)
plt.plot(x, 'bo', label='raw data')
plt.legend()
plt.show()