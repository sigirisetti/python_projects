import numpy as np

a = np.array([1,2,3])
print(a)
print(a.dtype)

b=np.array([(1,2,3), (4,5,6)])
print(b)
print(b.ndim)
print(b.shape)
print(b.dtype)

c=np.array([[1,2,3], [4,5,6]])
print(c)
print(c.ndim)
print(c.shape)
print(c.dtype)

d=np.array([(1,2,3), (4,5)]) # not homogenious
print(d)
print(d.ndim)
print(d.shape)
print(d.dtype)


# Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
a = np.array( [20,30,40,50] )
b = np.arange(4)

#applied elementwise and creates new array c
c = a - b
print(b**2)
print(10*np.sin(a))



c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
                [ 10, 12, 13]],
               [[100,101,102],
                [110,112,113]]])

c.shape
c[1,...]                                   # same as c[1,:,:] or c[1]
c[...,2]                                   # same as c[:,:,2]
