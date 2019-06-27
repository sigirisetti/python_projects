import numpy as np

B = np.arange(3)

print(B)
print(np.exp(B))
print(np.sqrt(B))

C = np.array([2., -1., 4.])
print(np.add(B, C))

#
# Boolean ufuncs
#

# all
print(np.all([[True,False],[True,True]]))
print(np.all([[True,False],[True,True]], axis=0))
print(np.all([-1, 4, 5]))
# Not a Number (NaN), positive infinity and negative infinity evaluate to True because these are not equal to zero.
print(np.all([1.0, np.nan]))

# any
print(np.any([[True, False], [False, False]], axis=0))

# cov
x = np.array([[0, 2], [1, 1], [2, 0]]).T
print(np.cov(x))


#See also
# all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross,
# cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer,
# prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where