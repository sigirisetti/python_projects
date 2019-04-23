def factor_count(N):
    cnt = 0
    i = 1
    factors = []
    while i * i <= N:
        if N % i == 0:
            factors.append(i)
            if i * i == N:
                cnt += 1
            else:
                cnt += 2
                factors.append(N//i)
        i += 1
    return factors


print(factor_count(1080))
