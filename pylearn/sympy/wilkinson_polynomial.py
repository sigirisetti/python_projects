from sympy import Symbol, Poly
from sympy.polys.polytools import poly_from_expr

x = Symbol('x')
W = 1
for i in range(1, 21):
    W = W * (x-i)

print(W.expand())

P,d = poly_from_expr(W.expand())
print(P)