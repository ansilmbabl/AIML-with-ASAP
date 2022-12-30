import numpy as np

#string array
sa=np.array([1,2,3],dtype="<U")

sa
array(['1', '2', '3'], dtype='<U1')

sa=np.array([1,2,3654],dtype="<U")
sa
array(['1', '2', '3654'], dtype='<U4')

sa=np.array([1,236546,3654],dtype="<U")
sa
array(['1', '236546', '3654'], dtype='<U6')



#complex numbers array
sa=np.array([1,236546,3654],dtype=complex)
sa
array([1.00000e+00+0.j, 2.36546e+05+0.j, 3.65400e+03+0.j])



##convertuing float to int
ia=np.array([1,23.6546,3.654],dtype=int)
ia
array([ 1, 23,  3])

ia=np.array([1,23.6546,3.999],dtype=int)
ia
array([ 1, 23,  3])



#array with zeros(color black)
az=np.zeros((3,3))
az
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])

az=np.zeros((3,3),dtype=int)
az
array([[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]])

az.dtype
dtype('int32')



#array with ones(color white)
ao=np.ones((3,3))
ao
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])

ao=np.ones((3,3),dtype=int)*255
ao
array([[255, 255, 255],
       [255, 255, 255],
       [255, 255, 255]])

ao.dtype
dtype('int32')

ao=np.ones((3,3),dtype=np.int16)*255
ao
array([[255, 255, 255],
       [255, 255, 255],
       [255, 255, 255]], dtype=int16)



#creating seq of numbers
np.arange(10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

np.arange(2,11)
array([ 2,  3,  4,  5,  6,  7,  8,  9, 10])

np.arange(2,11,2)
array([ 2,  4,  6,  8, 10])

np.arange(2,11,-1)
array([], dtype=int32)

np.arange(10,1,-1)
array([10,  9,  8,  7,  6,  5,  4,  3,  2])



#negative indexing
l=np.arange(0,10,2)
l
array([0, 2, 4, 6, 8])

l[-3]
4

#floating point
np.arange(0,1,.1)
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

#linspace
np.linspace(0,2,11)
array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8, 2. ])

#rshape array
a=np.arange(0,8)
a
array([0, 1, 2, 3, 4, 5, 6, 7])

b=a.reshape(2,4)
b
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])

td=np.arange(36).reshape(2,6,3)
td
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26],
        [27, 28, 29],
        [30, 31, 32],
        [33, 34, 35]]])

td[1][3][2]
29

td[1][2]
array([24, 25, 26])
