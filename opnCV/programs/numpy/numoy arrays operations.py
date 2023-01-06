Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=np.array([10,20,30,40])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=np.array([10,20,30,40])
NameError: name 'np' is not defined
import numpy as np
a=np.array([10,20,30,40])
b=np.arange(4)
b
array([0, 1, 2, 3])
a
array([10, 20, 30, 40])
c=a+b
c
array([10, 21, 32, 43])
d=a-b
d
array([10, 19, 28, 37])
e=a**2
e
array([ 100,  400,  900, 1600])
b<2
array([ True,  True, False, False])
f=a*b
f
array([  0,  20,  60, 120])
x=np.arange(3,7)
x
array([3, 4, 5, 6])
y=np.arange(10,13)
y
array([10, 11, 12])
q=x+y
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    q=x+y
ValueError: operands could not be broadcast together with shapes (4,) (3,) 
q=x-y
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    q=x-y
ValueError: operands could not be broadcast together with shapes (4,) (3,) 
q=x*y
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    q=x*y
ValueError: operands could not be broadcast together with shapes (4,) (3,) 
q=x**2
q
array([ 9, 16, 25, 36])
a=np.array([[1,2].[3,4]])
SyntaxError: invalid syntax
a=np.array([[1,2],[3,4]])
a
array([[1, 2],
       [3, 4]])
b=np.array([[5,6],[7,8]])
b
array([[5, 6],
       [7, 8]])
#element wise multiplicaton
a*b
array([[ 5, 12],
       [21, 32]])
#matrix multiplication
a@b
array([[19, 22],
       [43, 50]])
a.dot(b)
array([[19, 22],
       [43, 50]])
#random array generation
import random
random.randomint(1,100)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    random.randomint(1,100)
AttributeError: module 'random' has no attribute 'randomint'. Did you mean: 'randint'?
random.randint(1,100)
50
l=[1,2,3,4,5,6,78,9]
random.choice(l)
2
s="shydtfujasdyhf"
random.choice(s)
'y'
#random array
np.random.rand(2,3)
array([[0.71593823, 0.39145006, 0.3181498 ],
       [0.07800923, 0.94324321, 0.84380377]])
np.random.rand(2,3)
array([[0.32216601, 0.42817895, 0.91663371],
       [0.50771379, 0.79458379, 0.7644841 ]])
np.random.rand(2,3)*10
array([[4.385661  , 7.8833645 , 4.50791275],
       [0.23286885, 0.18795066, 0.82114197]])
a=np.random.rand(2,3)*10
a
array([[3.49245863, 8.7752955 , 6.83704195],
       [0.02689078, 6.35652147, 9.11724244]])
a.sum()
34.605450766042935
a.min()
0.02689077642364479
a.max()
9.117242435239039
a.dtype==int
False
a,dtype==int
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a,dtype==int
NameError: name 'dtype' is not defined. Did you mean: 'type'?
a=np.arange(18).reshape(3,6)
a
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17]])
a.sum(axis=0)
array([18, 21, 24, 27, 30, 33])
a.sum(axis=1)
array([15, 51, 87])
# axis 0= height
# axis 1= width
a.sum(axis=2)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.sum(axis=2)
  File "F:\Python 3.11\Lib\site-packages\numpy\core\_methods.py", line 49, in _sum
    return umr_sum(a, axis, dtype, out, keepdims, initial, where)
numpy.AxisError: axis 2 is out of bounds for array of dimension 2
b=np.arange(18).reshape(3,3,2)
b
array([[[ 0,  1],
        [ 2,  3],
        [ 4,  5]],

       [[ 6,  7],
        [ 8,  9],
        [10, 11]],

       [[12, 13],
        [14, 15],
        [16, 17]]])
b.sum(axis=0)
array([[18, 21],
       [24, 27],
       [30, 33]])
b.sum(axis=1)
array([[ 6,  9],
       [24, 27],
       [42, 45]])
b.sum(axis=2)
array([[ 1,  5,  9],
       [13, 17, 21],
       [25, 29, 33]])
a.cumsum(axis=1)
array([[ 0,  1,  3,  6, 10, 15],
       [ 6, 13, 21, 30, 40, 51],
       [12, 25, 39, 54, 70, 87]])
a.cumsum(axis=0)
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  8, 10, 12, 14, 16],
       [18, 21, 24, 27, 30, 33]])
a=np.array([1,2,3,4])
np.sin(a)
array([ 0.84147098,  0.90929743,  0.14112001, -0.7568025 ])
np.sqrt(a)
array([1.        , 1.41421356, 1.73205081, 2.        ])
a=np.arange(10)
a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a[4]
4
a=np.arange(10)*5
a[4]
20
a[::]
array([ 0,  5, 10, 15, 20, 25, 30, 35, 40, 45])
a[1:]
array([ 5, 10, 15, 20, 25, 30, 35, 40, 45])
a[:5]
array([ 0,  5, 10, 15, 20])
a[:7:3]
array([ 0, 15, 30])
a[::-1]
array([45, 40, 35, 30, 25, 20, 15, 10,  5,  0])
for i in a:
    print(i*4,end=" ")

    
0 20 40 60 80 100 120 140 160 180 
for i in a:
    print(i*4,end="x")

    
0x20x40x60x80x100x120x140x160x180x
a=np.floor(10*np.random.rand(3,4))
a
array([[2., 1., 1., 1.],
       [2., 2., 9., 6.],
       [2., 3., 6., 3.]])
a.ravel()
array([2., 1., 1., 1., 2., 2., 9., 6., 2., 3., 6., 3.])
b=np.ceil(10*np.random.rand(3,4))
b
array([[ 1.,  2.,  8.,  1.],
       [ 7., 10.,  8.,  5.],
       [ 8.,  1.,  8.,  4.]])
b.ravel()
array([ 1.,  2.,  8.,  1.,  7., 10.,  8.,  5.,  8.,  1.,  8.,  4.])
a.reshape(2,6)
array([[2., 1., 1., 1., 2., 2.],
       [9., 6., 2., 3., 6., 3.]])
a.T #transpose
array([[2., 2., 2.],
       [1., 2., 3.],
       [1., 9., 6.],
       [1., 6., 3.]])
np.transpose(a)
array([[2., 2., 2.],
       [1., 2., 3.],
       [1., 9., 6.],
       [1., 6., 3.]])
a
array([[2., 1., 1., 1.],
       [2., 2., 9., 6.],
       [2., 3., 6., 3.]])
a[1]
array([2., 2., 9., 6.])
a[::-1]
array([[2., 3., 6., 3.],
       [2., 2., 9., 6.],
       [2., 1., 1., 1.]])
a[0:1:-1]
array([], shape=(0, 4), dtype=float64)
a[1:0:-1]
array([[2., 2., 9., 6.]])
a[1][0]
2.0
a[1][::-1]
array([6., 9., 2., 2.])
a[::][::-1]
array([[2., 3., 6., 3.],
       [2., 2., 9., 6.],
       [2., 1., 1., 1.]])
a[::-1][::-1]
array([[2., 1., 1., 1.],
       [2., 2., 9., 6.],
       [2., 3., 6., 3.]])
