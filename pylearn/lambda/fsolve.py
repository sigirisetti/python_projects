from scipy.optimize import fsolve
import numpy as np

sol, = fsolve(lambda x: 2.5 - np.sqrt(x), 8)
print(sol)