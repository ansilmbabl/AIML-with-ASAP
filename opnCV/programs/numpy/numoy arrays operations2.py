Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
np.arange(12)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
a.reshape(3,4)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.reshape(3,4)
NameError: name 'a' is not defined
a=np.arange(12)
a.reshape(3,4)
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
b=np.transpose(a)
b
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
a=a.reshape(3,4)
a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
b=np.transpose(a)
b
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
np.append(b,[[1.,2.,3.]],axis=0)
array([[ 0.,  4.,  8.],
       [ 1.,  5.,  9.],
       [ 2.,  6., 10.],
       [ 3.,  7., 11.],
       [ 1.,  2.,  3.]])
b
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
c=np.array([6.,7.,8.,9.])
c
array([6., 7., 8., 9.])
c=c.reshape(4,1)
c
array([[6.],
       [7.],
       [8.],
       [9.]])
np.append(b,c,axis=1)
array([[ 0.,  4.,  8.,  6.],
       [ 1.,  5.,  9.,  7.],
       [ 2.,  6., 10.,  8.],
       [ 3.,  7., 11.,  9.]])
d=np.append(b,c,axis=1)
d
array([[ 0.,  4.,  8.,  6.],
       [ 1.,  5.,  9.,  7.],
       [ 2.,  6., 10.,  8.],
       [ 3.,  7., 11.,  9.]])
#stacking arrays

a=np.floor(10*np.random.rand(3,4))
a
array([[9., 1., 1., 6.],
       [4., 9., 9., 6.],
       [2., 2., 5., 0.]])
b=np.floor(10*np.random.rand(3,4))
b
array([[2., 5., 8., 1.],
       [2., 2., 2., 6.],
       [5., 3., 2., 8.]])
np.vstack((a,b))
array([[9., 1., 1., 6.],
       [4., 9., 9., 6.],
       [2., 2., 5., 0.],
       [2., 5., 8., 1.],
       [2., 2., 2., 6.],
       [5., 3., 2., 8.]])
np.vstack((b,a))
array([[2., 5., 8., 1.],
       [2., 2., 2., 6.],
       [5., 3., 2., 8.],
       [9., 1., 1., 6.],
       [4., 9., 9., 6.],
       [2., 2., 5., 0.]])
np.hstack((b,a))
array([[2., 5., 8., 1., 9., 1., 1., 6.],
       [2., 2., 2., 6., 4., 9., 9., 6.],
       [5., 3., 2., 8., 2., 2., 5., 0.]])
np.hstack((a,b))
array([[9., 1., 1., 6., 2., 5., 8., 1.],
       [4., 9., 9., 6., 2., 2., 2., 6.],
       [2., 2., 5., 0., 5., 3., 2., 8.]])
#splitting

a=np.floor(10*np.random.rand(3,12))
a
array([[5., 0., 9., 6., 3., 8., 2., 4., 0., 6., 4., 2.],
       [7., 8., 4., 9., 1., 3., 9., 9., 8., 6., 3., 0.],
       [6., 4., 3., 7., 6., 4., 8., 5., 7., 1., 3., 7.]])
np.hsplit(a,3)
[array([[5., 0., 9., 6.],
       [7., 8., 4., 9.],
       [6., 4., 3., 7.]]), array([[3., 8., 2., 4.],
       [1., 3., 9., 9.],
       [6., 4., 8., 5.]]), array([[0., 6., 4., 2.],
       [8., 6., 3., 0.],
       [7., 1., 3., 7.]])]
np.vsplit(a,2)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    np.vsplit(a,2)
  File "<__array_function__ internals>", line 200, in vsplit
  File "F:\Python 3.11\Lib\site-packages\numpy\lib\shape_base.py", line 997, in vsplit
    return split(ary, indices_or_sections, 0)
  File "<__array_function__ internals>", line 200, in split
  File "F:\Python 3.11\Lib\site-packages\numpy\lib\shape_base.py", line 872, in split
    raise ValueError(
ValueError: array split does not result in an equal division
np.vsplit(a,1)
[array([[5., 0., 9., 6., 3., 8., 2., 4., 0., 6., 4., 2.],
       [7., 8., 4., 9., 1., 3., 9., 9., 8., 6., 3., 0.],
       [6., 4., 3., 7., 6., 4., 8., 5., 7., 1., 3., 7.]])]
np.vsplit(a,3)
[array([[5., 0., 9., 6., 3., 8., 2., 4., 0., 6., 4., 2.]]), array([[7., 8., 4., 9., 1., 3., 9., 9., 8., 6., 3., 0.]]), array([[6., 4., 3., 7., 6., 4., 8., 5., 7., 1., 3., 7.]])]

#view or shallow copy
a=arange(4).rehsape(2,2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a=arange(4).rehsape(2,2)
NameError: name 'arange' is not defined. Did you mean: 'range'?
a=np.arange(4).rehsape(2,2)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a=np.arange(4).rehsape(2,2)
AttributeError: 'numpy.ndarray' object has no attribute 'rehsape'. Did you mean: 'reshape'?
a=(np.arange(4)).rehsape(2,2)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a=(np.arange(4)).rehsape(2,2)
AttributeError: 'numpy.ndarray' object has no attribute 'rehsape'. Did you mean: 'reshape'?
a=np.arange(4).reshape(2,2)
a
array([[0, 1],
       [2, 3]])
b=a.view()
b
array([[0, 1],
       [2, 3]])
b[0,1]=55
b
array([[ 0, 55],
       [ 2,  3]])
a
array([[ 0, 55],
       [ 2,  3]])
c.copy()
array([[6.],
       [7.],
       [8.],
       [9.]])
c=a.copy
x
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    x
NameError: name 'x' is not defined
c
<built-in method copy of numpy.ndarray object at 0x00000224D3627A50>
c
<built-in method copy of numpy.ndarray object at 0x00000224D3627A50>
c
<built-in method copy of numpy.ndarray object at 0x00000224D3627A50>
a
array([[ 0, 55],
       [ 2,  3]])
b
array([[ 0, 55],
       [ 2,  3]])
c=b.copy
c
<built-in method copy of numpy.ndarray object at 0x00000224D35BFB10>
b[0][1]
55
b[0,1]
55
b[0][1]=22
b
array([[ 0, 22],
       [ 2,  3]])
c=b.copy()
c
array([[ 0, 22],
       [ 2,  3]])
c
array([[ 0, 22],
       [ 2,  3]])
c[0,0]=45
c
array([[45, 22],
       [ 2,  3]])
a
array([[ 0, 22],
       [ 2,  3]])
b
array([[ 0, 22],
       [ 2,  3]])
