from datastructuresandalgorithms.numbers.gcd import gcd

def hasSameFactors(p, q):
    if p == q == 0:
        return True

    denom = gcd(p, q)

    while (p != 1):
        p_gcd = gcd(p, denom)
        if p_gcd == 1:
            break
        p /= p_gcd
    else:
        while (q != 1):
            q_gcd = gcd(q, denom)
            if q_gcd == 1:
                break
            q /= q_gcd
        else:
            return True

    return False


def solution(A, B):
    if len(A) != len(B):
        raise Exception("Invalid input")
    cnt = 0
    for idx in range(len(A)):
        if A[idx] < 0 or B[idx] < 0:
            raise Exception("Invalid value")
        if hasSameFactors(A[idx], B[idx]):
            cnt += 1

    return cnt


print(hasSameFactors(120, 150))
# print(gcd(10, 150))