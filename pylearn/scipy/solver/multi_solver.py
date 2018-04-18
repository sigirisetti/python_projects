from scipy.optimize import fsolve

def objective(X):
    x, y = X            # unpack the array in the argument
    z1 = y - x**2       # first equation
    z2 = y - 8 + x**2   # second equation
    return [z1, z2]     # list of zeros

x0, y0 = 1, 1           # initial guesses
guess = [x0, y0]
sol = fsolve(objective, guess)
print(sol)

# of course there may be more than one solution
x0, y0 = -1, -1           # initial guesses
guess = [x0, y0]
sol = fsolve(objective, guess)
print(sol)