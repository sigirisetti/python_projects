from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

k = 2.2


def myode(y, t):
    """ode defining exponential growth"""
    return k * y

y0 = 3
tspan = np.linspace(0,1)
y = odeint(myode, y0, tspan)

print(np.shape(y))

for x1,y1 in zip(tspan, y[:,0]):
    print ("x1 = ", x1, ", y1 = ", y1)

plt.plot(tspan, y)
plt.xlabel('Time')
plt.ylabel('y')
plt.show()