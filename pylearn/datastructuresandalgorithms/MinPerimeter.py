import math

def solution(N):
    if N <= 0:
        return 0

    for i in range(int(math.sqrt(N)), 0, -1):
        if N % i == 0:
            return 2 * (i + N / i)

    raise Exception("should never reach here!")

for i in range(10):
    print(i, solution(i))