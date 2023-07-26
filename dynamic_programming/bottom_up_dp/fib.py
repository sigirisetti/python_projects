import time


def fib(n):
    a = 1
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b

    return b


t0 = time.time()
print(fib(100))
t1 = time.time()

print("Time taken : ", '{:f}'.format(t1 - t0))
