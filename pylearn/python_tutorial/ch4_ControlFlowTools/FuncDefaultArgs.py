# Default args are only initialized once
i = 5


def f(arg=i):
    print(arg)

i = 6 # Initialized only once
f()


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))