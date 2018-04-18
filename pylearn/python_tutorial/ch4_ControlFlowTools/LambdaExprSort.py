pairs = [(2, 'two'), (1, 'one'), (3, 'three'), (4, 'four')]
# Sort by Value
pairs.sort(key=lambda pair: pair[1])
print(pairs)
# Sort by Key
pairs.sort(key=lambda pair: pair[0])
print(pairs)