from sympy import Function, Symbol, dsolve
f = Function('f')
x = Symbol('x')
fprime = f(x).diff(x) - f(x) # f' = f(x)

y = dsolve(fprime, f(x))

print(y)
print(y.subs(x,4))
print([y.subs(x, X) for X in [0, 0.5, 1]]) # multiple values