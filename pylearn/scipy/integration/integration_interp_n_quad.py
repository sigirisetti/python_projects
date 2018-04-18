from scipy.interpolate import interp1d
from scipy.integrate import quad
import numpy as np

x = [0, 0.5, 1, 1.5, 2]
y = [0,    0.1250,    1.0000,    3.3750,    8.0000]

f = interp1d(x, y)

# numerical trapezoid method
xfine = np.linspace(0.25, 1.75)
yfine = f(xfine)
print(np.trapz(yfine, xfine))

# quadrature with interpolation
ans, err = quad(f, 0.25, 1.75)
print(ans)