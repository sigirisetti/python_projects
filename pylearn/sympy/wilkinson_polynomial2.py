import numpy as np
from sympy import Symbol
from sympy.polys.polytools import poly_from_expr

x = Symbol('x')
W = 1
for i in range(1, 21):
    W = W * (x-i)

P,d = poly_from_expr(W.expand())
p = P.all_coeffs()
x = np.arange(1, 21)
print('\nThese are the known roots\n',x)

# evaluate the polynomial at the known roots
print('\nThe polynomial evaluates to {0} at the known roots'.format(np.polyval(p, x)))

# find the roots ourselves
roots = np.roots(p)
print('\nHere are the roots from numpy:\n', roots)

# evaluate solution at roots
print('\nHere is the polynomial evaluated at the calculated roots:\n', np.polyval(p, roots))