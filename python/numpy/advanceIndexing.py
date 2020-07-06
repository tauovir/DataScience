# -*- coding: utf-8 -*-
import pandas as pd
import numpy as  np

# Advanced indexing always returns a copy of the data. As against this, the slicing only presents a view.
x = np.array([[1,2],[3,4],[5,6]])
print(x)
y = x[[0,1,2],[0,1,0]]
y
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
x
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
y
# Sclicing
z = x[1:4,1:3]
z

# Using advanced index for columns
y = x[1:4,[1,2]]
y

#Boolean Array index
data = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
print("Item greater than 5")
print(data[data>5])

a = np.array([np.nan,1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])
