
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print('---------- 3 chunks')
for chunk in chunker(list, 3):
    print(chunk)

print('---------- 4 chunks')
for chunk in chunker(list, 4):
    print(chunk)

print('---------- 5 chunks')
for chunk in chunker(list, 5):
    print(chunk)

print('---------- 6 chunks')
for chunk in chunker(list, 6):
    print(chunk)

print('---------- 7 chunks')
for chunk in chunker(list, 7):
    print(chunk)

print('---------- 8 chunks')
for chunk in chunker(list, 8):
    print(chunk)

