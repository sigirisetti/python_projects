# Some operations, such as +=, -=, /=, and *=, act in place to modify an existing array rather than create a new one.

import numpy as np

a = np.ones((2,3), dtype=int)

b = np.random.random((2,3))

print("id(a) = ", id(a))
print("id(b) = ", id(b))

a *= 3
print("id(a) = ", id(a))

b += a
print("id(b) = ", id(b))


# a += b                  # b is not automatically converted to integer type
# TypeError: Cannot cast ufunc add output from dtype('float64') to dtype('int64') with casting rule 'same_kind'