# -*- coding: utf-8 -*-
import numpy as np

#This array attribute returns a tuple consisting of array dimensions. It can also be used to resize the array.
a = np.array([[1,2,3],[10,20,30]])
print(a)
print(a.shape)

arrb = np.array([[1,2,3],[4,5,6]]) 
b = arrb.reshape(3,2)
b

arng = np.arange(24)
arng
arng.ndim
bb = arng.reshape(2,4,3)
bb

bb = arng.reshape(6,4)
bb
bb.itemsize#This array attribute returns the length of each element of array in bytes

bb.flags





