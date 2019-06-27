"""
Count number of set bits in a integer
"""
def bit_count(num):
    if num == 0:
        return 0;

    count = 0;
    while num > 0:
        num = num & (num - 1)
        count += 1

    return count


print(bit_count(2))
print(bit_count(3))
print(bit_count(4))
print(bit_count(5))
print(bit_count(6))
print(bit_count(7))
