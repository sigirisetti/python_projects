import numpy as np


a = np.arange(10)**3
print(a)

print(a[2])

print(a[2:5])

a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
print(a)

print(a[ : :-1])                                 # reversed a

for i in a:
    print(i**(1/3.))


#
# numpy array from function
#

def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
print(b)
print(b[2,3])
print(b[0:5, 1])                       # each row in the second column of b
print(b[ : ,1])                        # equivalent to the previous example
print(b[1:3, : ])                      # each column in the second and third row of b
