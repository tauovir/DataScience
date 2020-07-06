# -*- coding: utf-8 -*-

"""
The Python and NumPy indexing operators "[ ]" and attribute operator "." provide quick 
and easy access to Pandas data structures across a wide range of use cases.
.loc():Label based
.iloc():Integer based
.ix():Both Label and Integer based
"""
import pandas as pd
import numpy as np
#loc takes two single/list/range operator separated by ','. The first one indicates the row and the second one indicates columns.
df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
print(df)

print(df.loc[:,'A'])
print(df.loc[:,['A','C']])


# Select few rows for multiple columns, say list[]
print(df.loc[['a','b','f','h'],['A','C']])

# Select range of all Columns
print(df.loc['a': 'h'])
# getting Values with boolean array
print(df.loc['a']>0)
print(df.loc[:,'A']>0)
#======================================iloc()================================================
"""
Pandas provide various methods in order to get purely integer based indexing. Like python and numpy, these are 0-based indexing.
The various access methods are as follows −
An Integer
A list of integers
A range of values
"""
data1 = pd.DataFrame(np.random.randn(8,4), columns = ['A','B','C','D'])
# Select All row from Specific Comulns
data1.iloc[:,[0]]
#data1.iloc[:4]

# Inter Slicing
data1.iloc[:4]
data1.iloc[1:5,2:4]

# Slicing through list of values
data1.iloc[[1,3,5],[2,3]]
data1.iloc[1:3,:]
data1.iloc[:,:]
data1.iloc[:,1:3]
"""
.ix()
andas provides a hybrid method for selections and subsetting the object using the .ix() operator.
"""
data1.ix[:,'A']
data1.ix[:,0]





#Attribute Access
#Columns can be selected using the attribute operator '.'.
data1.A
data1['A']
#Note − We can pass a list of values to [ ] to select those columns.
data1[['A','B']]

