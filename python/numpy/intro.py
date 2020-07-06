# -*- coding: utf-8 -*-

import numpy as np
np.array
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
a = np.array([1,2,3])
a
b = np.array([[1,2],[50,60]])

b= np.array([1, 2, 3,4,5], ndmin = 3) 

b= np.array([1, 2, 3,4,5], dtype = complex)
b

# Data type
dt = np.dtype(np.int32)
dt
dt1 = np.dtype('i4')
dt1

dt = np.dtype([('age', np.int8)])
 dt

# 
 student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
 student
 data_arr = np.array([('khan',28,350),('Ganga',60,400)], dtype = student)
 print(data_arr)
 
 
