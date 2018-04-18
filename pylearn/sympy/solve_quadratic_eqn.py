from sympy import solve, symbols, pprint

a, b, c, x = symbols('a,b,c,x')

f = a*x**2 + b*x + c

solution = solve(f, x)
print(solution)
pprint(solution)

from sympy import diff

print(diff(f, x))
print(diff(f, x, 2))

print(diff(f, a))

from sympy import integrate

print(integrate(f, x))          # indefinite integral
print(integrate(f, (x, 0, 1)))  # definite integral from x=0..1