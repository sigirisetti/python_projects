import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pycse import deriv

tspan = np.array([0, 0.1, 0.2, 0.4, 0.8, 1])
Ca_data = np.array([2.0081,  1.5512,  1.1903,  0.7160,  0.2562,  0.1495])

def func(t, Ca0, k):
    return Ca0 * np.exp(-k * t)


pars, pcov = curve_fit(func, tspan, Ca_data, p0=[2, 2.3])

print(pars)
print(pcov)

plt.plot(tspan, Ca_data)
plt.plot(tspan, func(tspan, *pars), 'g-')
plt.show()

# analytical derivative
k, Ca0 = pars
dCdt = -k * Ca0 * np.exp(-k * tspan)
t = np.linspace(0, 2)
dCdt_res =  -k * Ca0 * np.exp(-k * t)

plt.figure()
plt.plot(tspan, deriv(tspan, Ca_data), label='numerical derivative')
plt.plot(tspan, dCdt, label='analytical derivative of fit')
plt.plot(t, dCdt_res, label='extrapolated')
plt.legend(loc='best')
plt.show()