import numpy as np
import matplotlib.pyplot as plt
from pycse import deriv

tspan = [0, 0.1, 0.2, 0.4, 0.8, 1]
Ca_data = [2.0081,  1.5512,  1.1903,  0.7160,  0.2562,  0.1495]

p = np.polyfit(tspan, Ca_data, 3)
plt.figure()
plt.plot(tspan, Ca_data)
plt.plot(tspan, np.polyval(p, tspan), 'g-')
plt.show()

# compute derivatives
dp = np.polyder(p)

dCdt_fit = np.polyval(dp, tspan)

dCdt_numeric = deriv(tspan, Ca_data) # 2-point deriv

plt.figure()
plt.plot(tspan, dCdt_numeric, label='numeric derivative')
plt.plot(tspan, dCdt_fit, label='fitted derivative')

t = np.linspace(min(tspan), max(tspan))
plt.plot(t, np.polyval(dp, t), label='resampled derivative')
plt.legend(loc='best')
plt.show()