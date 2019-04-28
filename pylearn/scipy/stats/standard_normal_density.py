from scipy.stats import norm
from scipy.integrate import quad

ϕ = norm()

value, error = quad(ϕ.pdf, -1, 1)  # Integrate using Gaussian quadrature
print(value) #68%

value, error = quad(ϕ.pdf, -2, 2)  # Integrate using Gaussian quadrature
print(value) #95%

value, error = quad(ϕ.pdf, -3, 3)  # Integrate using Gaussian quadrature
print(value) #99%


value, error = quad(ϕ.pdf, 0, 10)  # Integrate using Gaussian quadrature
print(value) #50%