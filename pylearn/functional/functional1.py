import functools, operator


def func(*args):
    return functools.reduce(operator.add, args)

print(func(1, 2, 3, 4))