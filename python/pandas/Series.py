# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#Series is a one-dimensional array like structure with homogeneous data.
#Homogeneous data
#Size Immutable
#Values of Data Mutable
#pandas.Series( data, index, dtype, copy)

sr = pd.Series()
print(sr)

# Creating Series from Ndarray
data = np.array(['a','b','c','d','e'])
sr = pd.Series(data)
sr2 = pd.Series(data, index = [101,102,103,104,105])
print(sr2)

# Creating Series From Dictinary
data1 = {'name' : 'Khan','age': '27','salary':20}
sr3 = pd.Series(data1)
print(sr3)

# Creating Dictiinary from Scalar
s2 = pd.Series(6, index = [1,2,3,4,4,5,6])
print(s2)

# Accessing Data from Series
sr = pd.Series([1,2,3,4,5,6],index = [10,20,30,40,50,60])
print(sr[30])
print(sr[:3])# First 3 element
print(sr[-3:])# Last 3 element
sr = pd.Series([1,2,3,4,5,6],index = ['a','b','c','d','e','f'])
print(sr['c'])
# Retrivila of Multiple Variable
print(sr[['a','e']])



