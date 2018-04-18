import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

print(np.linspace(0, pi, 100))
plt.plot(np.linspace(0, pi, 100))
plt.ylabel('Pi Curve')
plt.show()