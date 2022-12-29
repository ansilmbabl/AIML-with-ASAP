import numpy as np 

a=np.array([[1,2,3],[4,5,6]])
print(a)
#[[1 2 3]
# [4 5 6]]
print(type(a))
#<class 'numpy.ndarray'>
print(a.ndim)
#2
print(a.size)
#6
print(a.shape)
#(2, 3)
print(a.dtype)
#int64
print(a.itemsize)
#8



af=np.array([1.0,2,3])
print(af)
#[[1. 2. 3.]
print(type(af))
#<class 'numpy.ndarray'>
print(af.ndim)
#1
print(af.size)
#3
print(af.shape)
#(3,)
print(af.dtype)
#float64
print(af.itemsize)
#8

